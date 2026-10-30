"""Bounded, unauthenticated HTTP page reader (``read_web_page``).

Fetched pages are untrusted data. Three rules are enforced in code rather than in
prose:

* the request carries no credentials of any kind, so a hostile or redirected page
  can never observe a model or search key;
* every target — the original URL and each redirect hop — is checked against the
  local/private/link-local address space before it is requested;
* name resolution never runs on the event loop, so a slow or hostile resolver can
  neither stall the pass nor outlive its budget.

An injected ``httpx.AsyncClient`` is treated as a *transport*, never as a source of
credentials or redirect policy. ``Client.stream()``/``build_request()`` merge the
client's own headers, cookies and auth into every request, and ``follow_redirects``
would issue the next hop before any guard could run. This module therefore sends a
bare ``httpx.Request`` through ``Client.send(..., auth=None, follow_redirects=False)``,
which carries only the headers set here — the same call shape on an injected and a
self-built client.
"""

from __future__ import annotations

import asyncio
import io
import ipaddress
import os
import re
import socket
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable
from urllib.parse import urljoin, urlparse

import httpx
from bs4 import BeautifulSoup, Comment

from enterprise_agent.tools.base import ToolError, ToolRecord, ToolResult

DEFAULT_TIMEOUT = 20.0
# SEC filings and modern pricing pages routinely exceed 1 MB, and a filing's
# balance sheet is far past the first 60k characters. The old limits turned a
# readable 10-K into a hard ``too_large`` failure or silently discarded its
# financial statements.
DEFAULT_MAX_BYTES = 8_000_000
DEFAULT_MAX_CHARS = 400_000
DEFAULT_MAX_REDIRECTS = 3
DEFAULT_DNS_TIMEOUT = 5.0
DEFAULT_MAX_PDF_PAGES = 60

ALLOWED_SCHEMES = frozenset({"http", "https"})
HTML_CONTENT_TYPES = frozenset({"text/html", "application/xhtml+xml", "text/plain"})
PDF_CONTENT_TYPES = frozenset({"application/pdf"})
TEXTUAL_CONTENT_TYPES = HTML_CONTENT_TYPES | PDF_CONTENT_TYPES
_PDF_MAGIC = b"%PDF-"

# SEC's fair-access policy rejects a product token without declared contact
# information (HTTP 403). This UA carries the project name and a contact URL but
# no credential. Operators can override it via ``WEB_READER_USER_AGENT``.
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (compatible; BusinessAgentResearch/0.2; "
    "+https://localhost/business-agent)"
)

# Status/codes for which a second, text-only read through a reader mirror is
# worth attempting. The mirror is an explicit opt-in (``WEB_READER_MIRROR``)
# because it sends the requested URL to a third-party service.
MIRROR_FALLBACK_CODES = frozenset({
    "http_error", "too_large", "blocked_page", "no_usable_text",
    "unsupported_content_type", "timeout", "network_error",
})

# Anti-bot interstitials often return HTTP 200 with a short page. Storing these
# as evidence is worse than recording a read failure: they would later look like
# official vendor text while saying nothing about the question.
_BLOCK_MARKERS = (
    "your request has been blocked",
    "access denied",
    "attention required! | cloudflare",
    "just a moment...",
    "enable javascript and cookies to continue",
    "client challenge",
    "please verify you are a human",
    "sorry, you have been blocked",
    "request unsuccessful",
)

Resolver = Callable[[str], list[str]]


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _system_resolver(host: str) -> list[str]:
    return [entry[4][0] for entry in socket.getaddrinfo(host, None)]


@dataclass(frozen=True)
class _Target:
    url: str
    host: str


class _ReadFailure(Exception):
    """Internal carrier so every failure becomes a normalized ``ToolResult``."""

    def __init__(self, code: str, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.retryable = retryable


async def _checked_target(url: str, resolver: Resolver, dns_timeout: float) -> _Target:
    """Accept only a credential-free HTTP(S) URL that resolves to public addresses."""

    candidate = url.strip()
    parsed = urlparse(candidate)

    scheme = parsed.scheme.lower()
    if scheme not in ALLOWED_SCHEMES:
        raise _ReadFailure("unsupported_scheme", f"only http and https URLs can be read, not {scheme or 'a relative URL'!r}")
    if parsed.username is not None or parsed.password is not None:
        raise _ReadFailure("unsupported_url", "URLs carrying embedded credentials are refused")

    host = parsed.hostname
    if not host:
        raise _ReadFailure("unsupported_url", "the URL has no host")
    try:
        port = parsed.port
    except ValueError as error:
        raise _ReadFailure("unsupported_url", "the URL has an unparseable port") from error
    if host != host.strip():
        raise _ReadFailure("unsupported_url", "the URL host contains whitespace")

    await _reject_non_public(host, resolver, dns_timeout)

    default_port = 443 if scheme == "https" else 80
    authority = f"[{host}]" if ":" in host else host
    netloc = authority if (port or default_port) == default_port else f"{authority}:{port}"
    rebuilt = parsed._replace(netloc=netloc, fragment="").geturl()
    return _Target(url=rebuilt, host=host)


async def _resolve_off_loop(host: str, resolver: Resolver, dns_timeout: float) -> list[str]:
    """Resolve ``host`` without blocking, with a bounded and cancellable wait.

    Boundary: a resolution already running in a worker thread cannot be interrupted
    — Python offers no way to kill a thread. What is guaranteed is that *this*
    coroutine stops waiting at the deadline, and that a timed-out or cancelled
    resolution is never followed by a fetch. The abandoned thread finishes on its
    own in the shared executor; it holds no page data and performs no request.
    """

    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, resolver, host)
    try:
        return await asyncio.wait_for(future, timeout=dns_timeout)
    except (asyncio.TimeoutError, TimeoutError) as error:
        future.cancel()
        raise _ReadFailure(
            "dns_timeout", f"resolving {host} exceeded the {dns_timeout:g}s resolution budget"
        ) from error
    except asyncio.CancelledError:
        # Propagate the cancellation; the caller must not go on to fetch.
        future.cancel()
        raise


async def _reject_non_public(host: str, resolver: Resolver, dns_timeout: float) -> None:
    """Block loopback, private, link-local, reserved and multicast targets."""

    if host.lower().rstrip(".") == "localhost":
        raise _ReadFailure("blocked_host", "the URL points at the local machine")

    try:
        literal = ipaddress.ip_address(host)
    except ValueError:
        literal = None

    if literal is not None:
        # An IP literal needs no resolution, so it never touches the loop or a thread.
        addresses = [literal]
    else:
        try:
            resolved = await _resolve_off_loop(host, resolver, dns_timeout)
        except _ReadFailure:
            raise
        except Exception as error:
            raise _ReadFailure("dns_error", f"the host could not be resolved: {host}") from error
        try:
            addresses = [ipaddress.ip_address(address) for address in resolved]
        except ValueError as error:
            raise _ReadFailure("dns_error", f"the host could not be resolved: {host}") from error
        if not addresses:
            raise _ReadFailure("dns_error", f"the host could not be resolved: {host}")

    # Any non-public address is disqualifying, even next to a public one: a host that
    # answers with both could be steered to the private address on a later request.
    # ``is_global`` alone is not enough — multicast ranges (224.0.0.0/4) report as
    # global in ``ipaddress`` but are not fetchable page hosts.
    def disqualifying(address: ipaddress.IPv4Address | ipaddress.IPv6Address) -> bool:
        return not address.is_global or address.is_multicast or address.is_reserved

    if any(disqualifying(address) for address in addresses):
        raise _ReadFailure("blocked_host", f"the URL resolves to a non-public address: {host}")


def _normalize(text: str) -> str:
    return " ".join(text.split())


def _mark_headings(container: BeautifulSoup | object) -> None:
    """Keep section headings in the flattened text.

    Without them a retrieved chunk can say "the add-on costs $200" while the only
    nearby product name lives in a heading, inviting a statement to be attributed
    to the wrong product. Markers survive whitespace normalization and are
    ordinary source text, so quote offsets stay exact.
    """
    for heading in container.find_all(["h1", "h2", "h3", "h4"]):
        label = _normalize(heading.get_text(" ", strip=True))
        if label:
            heading.replace_with(f" §{label}§ ")


def _extract_text(body: bytes, content_type: str, url: str) -> tuple[str, str, str]:
    """Return ``(text, title, region)`` for a textual response body."""

    if content_type == "text/plain":
        text = _normalize(body.decode("utf-8", errors="replace"))
        return text, url, "response body (plain text)"

    soup = BeautifulSoup(body.decode("utf-8", errors="replace"), "html.parser")
    for element in soup(["script", "style", "noscript", "template", "svg"]):
        element.decompose()
    for comment in soup.find_all(string=lambda value: isinstance(value, Comment)):
        comment.extract()

    title = ""
    if soup.title is not None and soup.title.string:
        title = _normalize(soup.title.string)

    for name in ("main", "article"):
        container = soup.find(name)
        if container is not None:
            _mark_headings(container)
            text = _normalize(container.get_text(" ", strip=True))
            if text:
                return text, title or url, f"<{name}> element"

    body_element = soup.body
    if body_element is not None:
        _mark_headings(body_element)
    text = _normalize(body_element.get_text(" ", strip=True) if body_element is not None else "")
    return text, title or url, "<body> element"


def _extract_pdf(body: bytes, url: str, max_pages: int) -> tuple[str, str, str, int]:
    """Extract page-marked text from a PDF; OCR is explicitly out of scope."""
    try:
        from pypdf import PdfReader
    except ImportError as error:  # pragma: no cover - dependency is declared
        raise _ReadFailure("pdf_support_unavailable", "PDF support requires the pypdf package") from error

    try:
        reader = PdfReader(io.BytesIO(body), strict=False)
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as error:
                raise _ReadFailure("pdf_encrypted", "the PDF is encrypted and cannot be read") from error
        total_pages = len(reader.pages)
        pages = []
        for index, page in enumerate(reader.pages[:max_pages], start=1):
            try:
                text = _normalize(page.extract_text() or "")
            except Exception:
                text = ""
            if text:
                pages.append(f"§PDF page {index}§ {text}")
        metadata = reader.metadata or {}
        title = metadata.get("/Title") if hasattr(metadata, "get") else None
        title = _normalize(title) if isinstance(title, str) and title.strip() else url
    except _ReadFailure:
        raise
    except Exception as error:
        raise _ReadFailure("pdf_extract_failed", "the PDF could not be parsed") from error

    if not pages:
        raise _ReadFailure(
            "no_usable_text",
            "the PDF contained no extractable text (scanned or image-only PDFs require OCR, which is unsupported)",
        )
    region = f"PDF pages 1-{min(total_pages, max_pages)} of {total_pages}"
    return _normalize(" ".join(pages)), title, region, min(total_pages, max_pages)


def _looks_blocked(text: str, title: str = "") -> bool:
    """Recognize short anti-bot interstitials that arrive with HTTP 200."""
    lowered = text.casefold()
    title_lowered = title.casefold()
    if len(text) > 4000:
        return False
    return any(marker in lowered or marker in title_lowered for marker in _BLOCK_MARKERS)


def _clean_mirror_text(body: bytes) -> tuple[str, str]:
    """Strip a reader mirror's metadata header while keeping its title."""
    raw = body.decode("utf-8", errors="replace")
    lines = raw.splitlines()
    title = ""
    for line in lines[:20]:
        if line.casefold().startswith("title:"):
            title = _normalize(line.split(":", 1)[1])
            break
    for index, line in enumerate(lines[:40]):
        if line.strip() in {"Markdown Content:", "Markdown"}:
            raw = "\n".join(lines[index + 1:])
            break
    return _normalize(raw), title


class WebPageReader:
    """Fetches one page and returns its visible text with provenance."""

    name = "read_web_page"

    def __init__(
        self,
        *,
        timeout: float = DEFAULT_TIMEOUT,
        max_bytes: int = DEFAULT_MAX_BYTES,
        max_chars: int = DEFAULT_MAX_CHARS,
        max_redirects: int = DEFAULT_MAX_REDIRECTS,
        dns_timeout: float = DEFAULT_DNS_TIMEOUT,
        max_pdf_pages: int = DEFAULT_MAX_PDF_PAGES,
        client: httpx.AsyncClient | None = None,
        resolver: Resolver | None = None,
        user_agent: str | None = None,
        mirror_prefix: str | None = None,
        mirror_timeout: float | None = None,
    ) -> None:
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        if max_bytes < 1:
            raise ValueError("max_bytes must be at least 1")
        if max_chars < 1:
            raise ValueError("max_chars must be at least 1")
        if max_redirects < 0:
            raise ValueError("max_redirects must not be negative")
        if dns_timeout <= 0:
            raise ValueError("dns_timeout must be positive")
        if max_pdf_pages < 1:
            raise ValueError("max_pdf_pages must be at least 1")
        if mirror_timeout is not None and mirror_timeout <= 0:
            raise ValueError("mirror_timeout must be positive")

        self._timeout = timeout
        self._max_bytes = max_bytes
        self._max_chars = max_chars
        self._max_redirects = max_redirects
        self._dns_timeout = dns_timeout
        self._max_pdf_pages = max_pdf_pages
        self._client = client
        self._resolver: Resolver = resolver or _system_resolver
        self._user_agent = (user_agent or os.getenv("WEB_READER_USER_AGENT", "")
                            or DEFAULT_USER_AGENT).strip()
        configured_mirror = (mirror_prefix if mirror_prefix is not None
                             else os.getenv("WEB_READER_MIRROR", ""))
        self._mirror_prefix = configured_mirror.strip().rstrip("/") or None
        # Rendering a blocked page through the mirror is slower than a direct GET.
        self._mirror_timeout = mirror_timeout or max(timeout * 2, 45.0)

    async def execute(self, query_or_input: str) -> ToolResult:
        requested = query_or_input.strip()
        if not requested:
            raise ValueError("page URL must not be blank")

        cost = {"page_calls": 1, "fetch_attempts": 0, "redirects": 0}
        try:
            if self._client is not None:
                return await self._read(self._client, requested, cost)
            async with httpx.AsyncClient(timeout=self._timeout) as client:
                return await self._read(client, requested, cost)
        except _ReadFailure as failure:
            return self._failed(requested, failure, cost)

    async def _read(self, client: httpx.AsyncClient, requested: str, cost: dict) -> ToolResult:
        try:
            return await self._read_direct(client, requested, cost)
        except _ReadFailure as failure:
            if not self._mirror_prefix or failure.code not in MIRROR_FALLBACK_CODES:
                raise
            try:
                return await self._read_mirror(client, requested, cost, failure)
            except _ReadFailure as mirror_failure:
                # Preserve both causes: a mirror failure alone would hide why the
                # primary request was not usable.
                raise _ReadFailure(
                    mirror_failure.code,
                    f"{mirror_failure.message} (direct read failed: {failure.code}: {failure.message})",
                ) from mirror_failure

    async def _read_direct(self, client: httpx.AsyncClient, requested: str, cost: dict) -> ToolResult:
        target = await _checked_target(requested, self._resolver, self._dns_timeout)

        for hop in range(self._max_redirects + 1):
            cost["fetch_attempts"] += 1
            response, body = await self._fetch(client, target.url, self._user_agent)
            if response.status_code in (301, 302, 303, 307, 308):
                location = response.headers.get("location")
                if not location:
                    raise _ReadFailure("http_error", f"the page returned HTTP {response.status_code} without a redirect target")
                # Each hop goes through the same guard as the original URL.
                target = await _checked_target(
                    urljoin(target.url, location), self._resolver, self._dns_timeout
                )
                cost["redirects"] = hop + 1
                continue

            if response.status_code >= 400:
                raise _ReadFailure("http_error", f"the page returned HTTP {response.status_code}")
            return self._record(requested, target.url, response, body, cost)

        raise _ReadFailure("too_many_redirects", f"the page exceeded {self._max_redirects} redirect(s)")

    async def _read_mirror(self, client: httpx.AsyncClient, requested: str,
                           cost: dict, direct_failure: _ReadFailure) -> ToolResult:
        """Read a text rendering through an explicitly configured reader mirror.

        The mirror is only used after the primary read produced no usable text.
        The recorded source URL stays the original page; the location records that
        the text came through a mirror so a reader can audit the acquisition path.
        """
        mirror_url = f"{self._mirror_prefix}/{requested}"
        target = await _checked_target(mirror_url, self._resolver, self._dns_timeout)
        response, body = await self._fetch(client, target.url, self._user_agent,
                                           timeout=self._mirror_timeout)
        if response.status_code >= 400:
            raise _ReadFailure("mirror_http_error",
                               f"the reader mirror returned HTTP {response.status_code}")
        return self._record_mirror(requested, response, body, cost, direct_failure)

    async def _fetch(self, client: httpx.AsyncClient, url: str,
                     user_agent: str,
                     timeout: float | None = None) -> tuple[httpx.Response, bytes]:
        # A bare Request carries only what is set here: no client headers, no cookies.
        # ``auth=None`` cancels the client's auth flow and ``follow_redirects=False``
        # stops httpx from issuing the next hop before the guard above can run.
        #
        # The timeout must be set explicitly too. A bare Request has no ``timeout``
        # extension, so an injected client configured with ``timeout=None`` would wait
        # forever; this reader's own bound is what the request has to carry.
        request = httpx.Request(
            "GET",
            url,
            headers={"User-Agent": user_agent,
                     "Accept": "text/html,text/plain;q=0.9,application/pdf;q=0.8,*/*;q=0.1",
                     "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8"},
            extensions={"timeout": httpx.Timeout(timeout or self._timeout).as_dict()},
        )
        try:
            response = await client.send(request, stream=True, auth=None, follow_redirects=False)
            try:
                chunks: list[bytes] = []
                total = 0
                async for chunk in response.aiter_bytes():
                    total += len(chunk)
                    if total > self._max_bytes:
                        raise _ReadFailure(
                            "too_large", f"the page exceeded the {self._max_bytes}-byte read limit"
                        )
                    chunks.append(chunk)
                return response, b"".join(chunks)
            finally:
                await response.aclose()
        except _ReadFailure:
            raise
        except httpx.TimeoutException as error:
            raise _ReadFailure("timeout", "the page did not answer within the timeout") from error
        except httpx.TransportError as error:
            raise _ReadFailure("network_error", "the page could not be reached") from error

    def _record(
        self, requested: str, url: str, response: httpx.Response, body: bytes, cost: dict
    ) -> ToolResult:
        content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
        is_pdf = (content_type in PDF_CONTENT_TYPES
                  or (content_type in {"application/octet-stream", ""} and body.startswith(_PDF_MAGIC)))
        if is_pdf:
            text, title, region, pages = _extract_pdf(body, url, self._max_pdf_pages)
            cost["pdf_pages"] = pages
        elif content_type in HTML_CONTENT_TYPES:
            text, title, region = _extract_text(body, content_type, url)
        else:
            # Images, archives and other media are out of scope rather than silently mangled.
            raise _ReadFailure(
                "unsupported_content_type",
                f"only HTML, plain text and PDF pages can be read, not {content_type or 'an unlabelled content type'!r}",
            )
        if not text:
            raise _ReadFailure("no_usable_text", "the page contained no extractable text")
        if _looks_blocked(text, title):
            raise _ReadFailure(
                "blocked_page",
                "the page returned an anti-automation interstitial instead of its content",
            )

        truncated = len(text) > self._max_chars
        # Strip after clipping so the recorded character count describes the stored text.
        content = (text[: self._max_chars] if truncated else text).strip()
        location = f"{region}; characters 0-{len(content)} of {len(text)}"
        if truncated:
            location = f"{location} (truncated at the {self._max_chars}-character limit)"

        cost.update(
            {
                "content_type": content_type or None,
                "extracted_chars": len(content),
                "total_chars": len(text),
                "truncated": truncated,
                "mirror": False,
            }
        )
        return ToolResult(
            tool_name=self.name,
            query_or_input=requested,
            records=[
                ToolRecord(
                    content=content,
                    source_url=url,
                    source_title=title,
                    source_location=location,
                    retrieved_at=_utcnow(),
                )
            ],
            cost_metadata=dict(cost),
        )

    def _record_mirror(self, requested: str, response: httpx.Response, body: bytes,
                       cost: dict, direct_failure: _ReadFailure) -> ToolResult:
        content_type = response.headers.get("content-type", "").split(";")[0].strip().lower()
        if content_type in HTML_CONTENT_TYPES and content_type != "text/plain":
            text, title, _ = _extract_text(body, content_type, requested)
        else:
            text, title = _clean_mirror_text(body)
        if not text:
            raise _ReadFailure("no_usable_text", "the reader mirror returned no usable text")
        if _looks_blocked(text, title):
            raise _ReadFailure("blocked_page", "the reader mirror returned an anti-automation page")

        truncated = len(text) > self._max_chars
        content = (text[: self._max_chars] if truncated else text).strip()
        kind = "PDF text mirror" if requested.casefold().split("?")[0].endswith(".pdf") else "text mirror"
        location = (f"{kind} (reader mirror); direct read failed: {direct_failure.code}; "
                    f"characters 0-{len(content)} of {len(text)}")
        if truncated:
            location = f"{location} (truncated at the {self._max_chars}-character limit)"
        cost.update({
            "content_type": content_type or None,
            "extracted_chars": len(content),
            "total_chars": len(text),
            "truncated": truncated,
            "mirror": True,
            "direct_error": direct_failure.code,
        })
        return ToolResult(
            tool_name=self.name,
            query_or_input=requested,
            records=[ToolRecord(content=content, source_url=requested,
                                source_title=title or requested,
                                source_location=location, retrieved_at=_utcnow())],
            cost_metadata=dict(cost),
        )

    def _failed(self, query: str, failure: _ReadFailure, cost: dict) -> ToolResult:
        cost.update({"extracted_chars": 0, "truncated": False})
        return ToolResult(
            tool_name=self.name,
            query_or_input=query,
            records=[],
            cost_metadata=dict(cost),
            error=ToolError(code=failure.code, message=failure.message, retryable=failure.retryable),
        )
