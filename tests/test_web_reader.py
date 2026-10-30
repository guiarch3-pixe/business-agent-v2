"""Mocked-HTTP tests for the bounded web page reader.

DNS is injected, so the SSRF guards are tested without any real name resolution
or network access.
"""

from __future__ import annotations

import asyncio
import time

import httpx
import pytest

from enterprise_agent.tools.web_reader import WebPageReader

HTML_PAGE = b"""
<html>
  <head>
    <title>  Accreditation   explained </title>
    <style>body { color: red; }</style>
    <script>window.tracker = "should not appear";</script>
  </head>
  <body>
    <nav>menu noise</nav>
    <main>
      <h1>Certification body accreditation</h1>
      <p>Accreditation is   an independent
         attestation of a conformity assessment body.</p>
    </main>
    <footer>footer noise</footer>
  </body>
</html>
"""


def _client(handler) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def _public_resolver(host: str) -> list[str]:
    return ["93.184.216.34"]


def _reader(handler, **kwargs) -> WebPageReader:
    kwargs.setdefault("resolver", _public_resolver)
    return WebPageReader(client=_client(handler), **kwargs)


def _html_response(content: bytes = HTML_PAGE, status: int = 200, url: str | None = None) -> httpx.Response:
    kwargs = {"headers": {"content-type": "text/html; charset=utf-8"}, "content": content}
    if url is not None:
        kwargs["request"] = httpx.Request("GET", url)
    return httpx.Response(status, **kwargs)


def test_html_extraction_keeps_visible_text_and_title():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return _html_response()

    result = asyncio.run(_reader(handler).execute("https://example.invalid/page"))

    assert result.error is None
    assert len(result.records) == 1
    record = result.records[0]
    assert record.source_title == "Accreditation explained"
    assert record.source_url == "https://example.invalid/page"
    assert "Accreditation is an independent attestation" in record.content
    assert "§Certification body accreditation§" in record.content
    assert "should not appear" not in record.content
    assert "color: red" not in record.content
    assert "menu noise" not in record.content
    assert "\n" not in record.content
    assert "  " not in record.content
    assert record.retrieved_at.tzinfo is not None


def test_reader_sends_no_credentials_of_any_kind():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return _html_response()

    asyncio.run(_reader(handler).execute("https://example.invalid/page"))
    headers = {name.lower(): value for name, value in captured["request"].headers.items()}
    assert "authorization" not in headers
    assert "cookie" not in headers
    assert "x-api-key" not in headers


def test_body_is_used_when_no_main_or_article_container_exists():
    page = b"<html><head><title>T</title></head><body><p>plain body text</p></body></html>"

    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response(page)

    result = asyncio.run(_reader(handler).execute("https://example.invalid/page"))
    assert result.records[0].content == "plain body text"
    assert "body" in result.records[0].source_location


def test_plain_text_response_is_accepted_without_html_parsing():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, headers={"content-type": "text/plain; charset=utf-8"}, content=b"line one\n\nline two"
        )

    result = asyncio.run(_reader(handler).execute("https://example.invalid/notes.txt"))
    assert result.error is None
    assert result.records[0].content == "line one line two"
    assert result.records[0].source_title == "https://example.invalid/notes.txt"


@pytest.mark.parametrize("content_type", ["image/png", "application/json"])
def test_unsupported_content_types_are_rejected(content_type):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": content_type},
                              content=b"not a readable research document")

    result = asyncio.run(_reader(handler).execute("https://example.invalid/file"))
    assert result.records == []
    assert result.error is not None
    assert result.error.code == "unsupported_content_type"


def _minimal_pdf(text: str = "Copilot Studio licensing guide. To purchase, customers must have "
                         "a qualifying Microsoft 365 plan.") -> bytes:
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
    ]
    stream = f"BT /F1 11 Tf 72 720 Td ({text}) Tj ET".encode()
    objects.append(b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
                   + stream + b"\nendstream")
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for index, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{index} 0 obj\n".encode() + body + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode() + b"0000000000 65535 f \n"
    for offset in offsets:
        out += f"{offset:010d} 00000 n \n".encode()
    out += (f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref}\n%%EOF\n").encode()
    return bytes(out)


@pytest.mark.parametrize("content_type", ["application/pdf", "application/octet-stream", ""])
def test_pdf_text_is_extracted_with_page_provenance(content_type):
    def handler(request: httpx.Request) -> httpx.Response:
        headers = {"content-type": content_type} if content_type else {}
        return httpx.Response(200, headers=headers, content=_minimal_pdf())

    result = asyncio.run(_reader(handler).execute("https://example.invalid/guide.pdf"))
    assert result.error is None
    record = result.records[0]
    assert "qualifying Microsoft 365 plan" in record.content
    assert record.content.startswith("§PDF page 1§")
    assert "PDF pages 1-1" in record.source_location
    assert result.cost_metadata["pdf_pages"] == 1


def test_invalid_pdf_is_a_structured_error_not_a_crash_or_an_html_page():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "application/pdf"},
                              content=b"%PDF-1.7 truncated")

    result = asyncio.run(_reader(handler).execute("https://example.invalid/broken.pdf"))
    assert result.records == []
    assert result.error is not None
    assert result.error.code in {"pdf_extract_failed", "no_usable_text"}


@pytest.mark.parametrize(
    "url",
    [
        "file:///etc/passwd",
        "ftp://example.invalid/x",
        "gopher://example.invalid/x",
        "javascript:alert(1)",
        "https://user:pass@example.invalid/x",
        "https://user@example.invalid/x",
        "https://:443/x",
    ],
)
def test_non_http_or_credential_bearing_urls_are_rejected(url):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _html_response()

    result = asyncio.run(_reader(handler).execute(url))
    assert result.error is not None
    assert result.error.code in {"unsupported_scheme", "unsupported_url"}
    assert calls == [], "a rejected URL must never be requested"


@pytest.mark.parametrize(
    "url",
    [
        "http://127.0.0.1:8000/admin",
        "http://localhost/x",
        "http://[::1]/x",
        "http://10.1.2.3/x",
        "http://192.168.0.1/x",
        "http://169.254.169.254/latest/meta-data/",
        "http://0.0.0.0/x",
        "http://224.0.0.1/x",
    ],
)
def test_local_and_private_targets_are_blocked_before_any_request(url):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _html_response()

    def resolver(host: str) -> list[str]:
        return ["93.184.216.34"]

    result = asyncio.run(_reader(handler, resolver=resolver).execute(url))
    assert calls == [], url
    assert result.error is not None
    assert result.error.code in {"blocked_host", "dns_error"}


def test_hostname_resolving_to_a_private_address_is_blocked():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _html_response()

    def resolver(host: str) -> list[str]:
        assert host == "internal.example.invalid"
        return ["10.0.0.7"]

    result = asyncio.run(_reader(handler, resolver=resolver).execute("https://internal.example.invalid/x"))
    assert calls == []
    assert result.error is not None and result.error.code == "blocked_host"


def test_hostname_resolving_to_a_mix_of_public_and_private_is_blocked():
    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response()

    def resolver(host: str) -> list[str]:
        return ["93.184.216.34", "127.0.0.1"]

    result = asyncio.run(_reader(handler, resolver=resolver).execute("https://mixed.example.invalid/x"))
    assert result.error is not None and result.error.code == "blocked_host"


def test_resolution_failure_is_reported_as_dns_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response()

    def resolver(host: str) -> list[str]:
        raise OSError("name resolution failed")

    result = asyncio.run(_reader(handler, resolver=resolver).execute("https://nope.invalid/x"))
    assert result.error is not None and result.error.code == "dns_error"


def test_each_redirect_target_is_checked_before_it_is_followed():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(302, headers={"location": "http://127.0.0.1/secret"})

    result = asyncio.run(_reader(handler).execute("https://example.invalid/redirect"))
    assert calls == ["https://example.invalid/redirect"]
    assert result.error is not None and result.error.code == "blocked_host"


def test_redirects_are_followed_manually_and_final_url_is_recorded():
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/start":
            return httpx.Response(301, headers={"location": "/final"})
        return _html_response()

    result = asyncio.run(_reader(handler).execute("https://example.invalid/start"))
    assert result.error is None
    assert result.records[0].source_url == "https://example.invalid/final"
    assert result.cost_metadata["redirects"] == 1
    assert result.query_or_input == "https://example.invalid/start"


def test_too_many_redirects_stop_the_read():
    def handler(request: httpx.Request) -> httpx.Response:
        step = int(request.url.path.strip("/") or 0)
        return httpx.Response(302, headers={"location": f"/{step + 1}"})

    result = asyncio.run(_reader(handler, max_redirects=2).execute("https://example.invalid/0"))
    assert result.error is not None and result.error.code == "too_many_redirects"
    assert result.records == []


def test_response_larger_than_the_byte_cap_is_an_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "text/html"}, content=b"<html><body>" + b"x" * 5000 + b"</body></html>")

    result = asyncio.run(_reader(handler, max_bytes=256).execute("https://example.invalid/big"))
    assert result.records == []
    assert result.error is not None and result.error.code == "too_large"


def test_extracted_text_is_truncated_and_the_clipping_is_recorded():
    page = b"<html><head><title>T</title></head><body><main>" + b"word " * 100 + b"</main></body></html>"

    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response(page)

    result = asyncio.run(_reader(handler, max_chars=40).execute("https://example.invalid/long"))
    record = result.records[0]
    # The limit is a cap, not an exact length: the clipped text is stripped before storage.
    assert len(record.content) <= 40
    assert result.cost_metadata["truncated"] is True
    assert result.cost_metadata["extracted_chars"] == len(record.content)
    assert result.cost_metadata["total_chars"] > 40
    assert "truncated" in record.source_location


def test_untruncated_page_is_marked_as_such():
    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response()

    result = asyncio.run(_reader(handler, max_chars=10000).execute("https://example.invalid/page"))
    assert result.cost_metadata["truncated"] is False
    assert "truncated" not in result.records[0].source_location


@pytest.mark.parametrize(
    "page",
    [
        b"<html><head><script>var a = 1;</script></head><body><style>p{}</style></body></html>",
        b"<html><body>   \n\t  </body></html>",
    ],
)
def test_page_without_usable_text_is_an_error(page):
    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response(page)

    result = asyncio.run(_reader(handler).execute("https://example.invalid/empty"))
    assert result.records == []
    assert result.error is not None and result.error.code == "no_usable_text"


@pytest.mark.parametrize("status", [400, 403, 404, 418, 500, 503])
def test_http_error_statuses_are_reported_without_a_body(status):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status, headers={"content-type": "text/html"}, content=b"<html><body>error page</body></html>")

    result = asyncio.run(_reader(handler).execute("https://example.invalid/nope"))
    assert result.records == []
    assert result.error is not None
    assert result.error.code == "http_error"
    assert str(status) in result.error.message
    assert "error page" not in result.error.message


def test_timeout_and_connection_failure_are_normalized():
    def timing_out(request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("slow", request=request)

    def refusing(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)

    timeout = asyncio.run(_reader(timing_out).execute("https://example.invalid/x"))
    assert timeout.error is not None and timeout.error.code == "timeout"

    network = asyncio.run(_reader(refusing).execute("https://example.invalid/x"))
    assert network.error is not None and network.error.code == "network_error"


def test_blank_url_and_invalid_limits_are_rejected():
    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response()

    reader = _reader(handler)
    with pytest.raises(ValueError):
        asyncio.run(reader.execute("  "))
    with pytest.raises(ValueError):
        WebPageReader(client=_client(handler), max_chars=0)
    with pytest.raises(ValueError):
        WebPageReader(client=_client(handler), max_bytes=0)
    with pytest.raises(ValueError):
        WebPageReader(client=_client(handler), max_redirects=-1)
    with pytest.raises(ValueError):
        WebPageReader(client=_client(handler), timeout=0)


def test_reader_name_matches_the_shared_contract():
    assert WebPageReader.name == "read_web_page"


# ------------------------------------------------- injected-client isolation (D1)
#
# An injected client is a transport convenience, not a source of credentials or
# redirect policy. Whatever the caller configured on it must not reach the wire.


def _leaky_client(handler) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        headers={"Authorization": "Bearer LEAKED", "X-Api-Key": "LEAKED"},
        cookies={"session": "LEAKED"},
        auth=("user", "LEAKED-PASSWORD"),
        follow_redirects=True,
    )


def test_injected_client_authorization_cookies_and_auth_are_never_sent():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return _html_response()

    result = asyncio.run(
        WebPageReader(client=_leaky_client(handler), resolver=_public_resolver).execute(
            "https://example.invalid/page"
        )
    )

    assert result.error is None
    sent = {name.lower(): value for name, value in captured["request"].headers.items()}
    assert "authorization" not in sent
    assert "cookie" not in sent
    assert "x-api-key" not in sent
    assert "LEAKED" not in " ".join(sent.values())


def test_injected_client_redirect_capability_does_not_bypass_the_address_guard():
    calls = []

    def handler(request: httpx.AsyncClient) -> httpx.Response:
        calls.append(str(request.url))
        return httpx.Response(302, headers={"location": "http://127.0.0.1/secret"})

    result = asyncio.run(
        WebPageReader(client=_leaky_client(handler), resolver=_public_resolver).execute(
            "https://example.invalid/start"
        )
    )

    # The client would have followed automatically; the reader must not.
    assert calls == ["https://example.invalid/start"]
    assert result.records == []
    assert result.error is not None and result.error.code == "blocked_host"


def test_injected_client_does_not_auto_follow_to_a_public_redirect_either():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "/final"})
        return _html_response()

    result = asyncio.run(
        WebPageReader(client=_leaky_client(handler), resolver=_public_resolver).execute(
            "https://example.invalid/start"
        )
    )

    # Same end state as before, but reached by the reader's own checked hop.
    assert calls == ["https://example.invalid/start", "https://example.invalid/final"]
    assert result.records[0].source_url == "https://example.invalid/final"
    assert result.cost_metadata["redirects"] == 1


def test_a_mid_chain_redirect_to_a_private_target_is_blocked():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(str(request.url))
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "/hop"})
        return httpx.Response(302, headers={"location": "http://10.0.0.5/internal"})

    result = asyncio.run(
        WebPageReader(client=_leaky_client(handler), resolver=_public_resolver).execute(
            "https://example.invalid/start"
        )
    )

    assert calls == ["https://example.invalid/start", "https://example.invalid/hop"]
    assert result.error is not None and result.error.code == "blocked_host"


# --------------------------------------------------- non-blocking DNS (D2)
#
# Address resolution must not run on the event loop. A slow resolver has to be
# bounded and cancellable, and cancellation must never be followed by a fetch.


def test_slow_resolver_does_not_block_the_event_loop():
    ticks = 0

    def resolver(host: str) -> list[str]:
        time.sleep(0.25)
        return ["93.184.216.34"]

    async def main() -> int:
        nonlocal ticks

        async def ticker() -> None:
            nonlocal ticks
            while True:
                await asyncio.sleep(0.01)
                ticks += 1

        task = asyncio.create_task(ticker())
        try:
            await WebPageReader(
                client=_client(lambda request: _html_response()), resolver=resolver, dns_timeout=5.0
            ).execute("https://slow.example.invalid/x")
        finally:
            task.cancel()
        return ticks

    # A blocking resolver holds the loop for its whole 0.25 s, so the ticker never runs.
    assert asyncio.run(main()) >= 5


def test_dns_wait_is_bounded_and_never_fetches_after_a_timeout():
    calls = []

    def resolver(host: str) -> list[str]:
        time.sleep(0.3)
        return ["93.184.216.34"]

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _html_response()

    async def main():
        reader = WebPageReader(client=_client(handler), resolver=resolver, dns_timeout=0.05)
        started = time.perf_counter()
        result = await reader.execute("https://slow.example.invalid/x")
        return result, time.perf_counter() - started

    result, elapsed = asyncio.run(main())

    assert result.error is not None and result.error.code == "dns_timeout"
    assert result.records == []
    assert calls == [], "a timed-out resolution must not be followed by a fetch"
    assert elapsed < 0.25, f"waited {elapsed:.3f}s; the bounded wait should return far sooner"


def test_an_outer_cancellation_during_dns_propagates_and_never_fetches():
    calls = []
    entered = asyncio.Event()

    def resolver(host: str) -> list[str]:
        entered.set()
        time.sleep(0.3)
        return ["93.184.216.34"]

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _html_response()

    async def main() -> None:
        reader = WebPageReader(client=_client(handler), resolver=resolver, dns_timeout=5.0)
        task = asyncio.create_task(reader.execute("https://slow.example.invalid/x"))
        await asyncio.wait_for(entered.wait(), timeout=2.0)
        await asyncio.sleep(0)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(main())
    assert calls == [], "a cancelled read must not go on to fetch the page"


def test_ip_literal_targets_skip_resolution_entirely():
    called = []

    def resolver(host: str) -> list[str]:
        called.append(host)
        return ["93.184.216.34"]

    result = asyncio.run(
        WebPageReader(client=_client(lambda request: _html_response()), resolver=resolver).execute(
            "https://93.184.216.34/page"
        )
    )
    assert result.error is None
    assert called == [], "an IP literal needs no resolution"


def test_dns_timeout_must_be_positive():
    with pytest.raises(ValueError):
        WebPageReader(client=_client(lambda request: _html_response()), dns_timeout=0)


# ------------------------------------------------ request timeout extensions (D3)
#
# A bare Request carries no ``timeout`` extension, so a client configured with
# ``timeout=None`` would let a page hang forever. The reader's own timeout must reach
# the request, while staying credential-free and hop-checked.


def test_reader_timeout_reaches_the_request_when_the_client_has_none():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["extensions"] = dict(request.extensions)
        return _html_response()

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=None)
    result = asyncio.run(
        WebPageReader(client=client, resolver=_public_resolver, timeout=0.25).execute(
            "https://example.invalid/x"
        )
    )

    assert result.error is None
    timeout = seen["extensions"].get("timeout")
    assert timeout is not None, "the request must carry an explicit timeout"
    for phase in ("connect", "read", "write", "pool"):
        assert timeout[phase] == pytest.approx(0.25), phase


def test_each_redirect_hop_carries_the_timeout_and_no_credentials():
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append((str(request.url), dict(request.extensions), dict(request.headers)))
        if request.url.path == "/start":
            return httpx.Response(302, headers={"location": "/final"})
        return _html_response()

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(handler),
        timeout=None,
        headers={"Authorization": "Bearer LEAKED"},
        follow_redirects=True,
    )
    asyncio.run(
        WebPageReader(client=client, resolver=_public_resolver, timeout=0.25).execute(
            "https://example.invalid/start"
        )
    )

    assert [url for url, _, _ in seen] == [
        "https://example.invalid/start",
        "https://example.invalid/final",
    ]
    for url, extensions, headers in seen:
        assert extensions.get("timeout", {}).get("read") == pytest.approx(0.25), url
        lowered = {name.lower() for name in headers}
        assert "authorization" not in lowered
        assert "cookie" not in lowered


def test_an_ip_literal_request_also_carries_the_timeout():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["extensions"] = dict(request.extensions)
        return _html_response()

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=None)
    asyncio.run(
        WebPageReader(client=client, resolver=_public_resolver, timeout=0.5).execute(
            "https://93.184.216.34/x"
        )
    )
    assert seen["extensions"]["timeout"]["read"] == pytest.approx(0.5)


def test_short_anti_bot_interstitial_is_not_returned_as_page_text():
    page = (b"<html><head><title>Your request has been blocked</title></head>"
            b"<body>Your request has been blocked. This could be due to several reasons.</body></html>")

    def handler(request: httpx.Request) -> httpx.Response:
        return _html_response(page)

    result = asyncio.run(_reader(handler).execute("https://example.invalid/blocked"))
    assert result.records == []
    assert result.error is not None and result.error.code == "blocked_page"


def test_mirror_fallback_records_the_original_url_and_the_acquisition_path():
    requested = "https://example.invalid/official-pricing"

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.host == "r.jina.ai":
            return httpx.Response(
                200,
                headers={"content-type": "text/plain; charset=utf-8"},
                content=("Title: Official pricing\n\nURL Source: " + requested +
                         "\n\nMarkdown Content:\nThe official price is $39.00 user/month.").encode(),
            )
        return httpx.Response(403, headers={"content-type": "text/html"}, content=b"blocked")

    result = asyncio.run(_reader(handler, mirror_prefix="https://r.jina.ai").execute(requested))

    assert result.error is None
    record = result.records[0]
    assert record.source_url == requested
    assert record.source_title == "Official pricing"
    assert "official price is $39.00" in record.content
    assert "text mirror" in record.source_location
    assert result.cost_metadata["mirror"] is True


def test_mirror_is_not_used_when_the_direct_read_succeeds():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.host)
        return _html_response()

    result = asyncio.run(_reader(handler, mirror_prefix="https://r.jina.ai").execute(
        "https://example.invalid/page"))

    assert result.error is None
    assert calls == ["example.invalid"]
    assert result.cost_metadata["mirror"] is False
