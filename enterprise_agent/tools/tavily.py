"""Tavily search adapter (``search_web``).

Search output is discovery material, not page evidence: the returned snippets are
labelled as snippets so a later reader cannot mistake them for fetched page text.

An empty result list is a successful search that found nothing. A malformed
provider response is an explicit error — the two must never collapse into the
same outcome, because "no results" and "the search broke" justify different
conclusions.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

import httpx

from enterprise_agent.tools.base import ToolError, ToolRecord, ToolResult

SEARCH_URL = "https://api.tavily.com/search"
DEFAULT_MAX_RESULTS = 3
DEFAULT_TIMEOUT = 20.0
SNIPPET_LOCATION = "search result snippet (discovery material, not page text)"


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TavilySearchTool:
    """Runs one bounded Tavily search per ``execute`` call."""

    name = "search_web"

    def __init__(
        self,
        api_key: str,
        *,
        max_results: int = DEFAULT_MAX_RESULTS,
        timeout: float = DEFAULT_TIMEOUT,
        search_depth: str = "basic",
        client: httpx.AsyncClient | None = None,
    ) -> None:
        if not api_key or not api_key.strip():
            raise ValueError("TavilySearchTool requires a non-blank api_key")
        if not 1 <= max_results <= 20:
            raise ValueError("max_results must be between 1 and 20")
        if timeout <= 0:
            raise ValueError("timeout must be positive")
        if search_depth not in {"basic", "advanced"}:
            raise ValueError("search_depth must be 'basic' or 'advanced'")

        self._api_key = api_key.strip()
        self._max_results = max_results
        self._timeout = timeout
        self._search_depth = search_depth
        self._client = client

    async def execute(self, query_or_input: str) -> ToolResult:
        query = query_or_input.strip()
        if not query:
            raise ValueError("search query must not be blank")

        body = {
            "query": query,
            "search_depth": self._search_depth,
            "max_results": self._max_results,
            "include_answer": False,
            "include_raw_content": False,
            "include_usage": True,
        }
        try:
            if self._client is not None:
                payload = await self._post(self._client, body)
            else:
                async with httpx.AsyncClient(timeout=self._timeout) as client:
                    payload = await self._post(client, body)
        except _SearchFailure as failure:
            return self._failed(query, failure.code, failure.message)
        return self._success(query, payload)

    async def _post(self, client: httpx.AsyncClient, body: dict[str, Any]) -> Any:
        try:
            response = await client.post(
                SEARCH_URL,
                json=body,
                headers={"Authorization": f"Bearer {self._api_key}"},
                timeout=self._timeout,
            )
        except httpx.TimeoutException as error:
            raise _SearchFailure("timeout", "the search provider did not answer within the timeout") from error
        except httpx.TransportError as error:
            raise _SearchFailure("network_error", "the search provider could not be reached") from error

        if response.status_code >= 400:
            raise _SearchFailure(*_failure_for_status(response.status_code))
        try:
            return response.json()
        except ValueError as error:
            raise _SearchFailure("invalid_response", "the search provider returned a non-JSON response") from error

    def _success(self, query: str, payload: Any) -> ToolResult:
        records: list[ToolRecord] = []
        # One retrieval timestamp for the whole response: the search is a single event.
        retrieved_at = _utcnow()

        if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
            return self._failed(query, "invalid_response", "the search provider returned an unexpected payload shape")

        for entry in payload["results"]:
            record = self._record_from(entry, retrieved_at)
            if isinstance(record, str):
                return self._failed(query, "invalid_response", record)
            records.append(record)

        return ToolResult(
            tool_name=self.name,
            query_or_input=query,
            records=records,
            cost_metadata={
                "search_calls": 1,
                "provider": "tavily",
                "result_count": len(records),
                "credits": _credit_usage(payload.get("usage")),
            },
        )

    def _record_from(self, entry: Any, retrieved_at: datetime) -> ToolRecord | str:
        if not isinstance(entry, dict):
            return "the search provider returned a result that was not an object"
        url = entry.get("url")
        title = entry.get("title")
        content = entry.get("content")
        if not isinstance(url, str) or not url.strip():
            return "the search provider returned a result without a URL"
        if not isinstance(title, str) or not title.strip():
            return "the search provider returned a result without a title"
        if not isinstance(content, str) or not content.strip():
            return "the search provider returned a result without any snippet text"
        try:
            return ToolRecord(
                content=content,
                source_url=url,
                source_title=title,
                source_location=SNIPPET_LOCATION,
                retrieved_at=retrieved_at,
            )
        except ValueError as error:
            # Rejecting the whole response is deliberate: skipping one malformed entry
            # would silently shrink the result set and look like "fewer sources exist".
            return f"the search provider returned an unusable result URL or snippet: {type(error).__name__}"

    def _failed(self, query: str, code: str, message: str) -> ToolResult:
        return ToolResult(
            tool_name=self.name,
            query_or_input=query,
            records=[],
            cost_metadata={"search_calls": 1, "provider": "tavily", "credits": None},
            error=ToolError(code=code, message=message, retryable=False),
        )


class _SearchFailure(Exception):
    """Internal carrier so provider failures become normalized results, not crashes."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def _failure_for_status(status: int) -> tuple[str, str]:
    if status in (401, 403):
        return "auth_error", f"the search provider rejected the credentials (HTTP {status})"
    if status == 429:
        return "rate_limited", "the search provider rate-limited the request (HTTP 429)"
    if status >= 500:
        return "server_error", f"the search provider failed with HTTP {status}"
    return "http_error", f"the search provider returned HTTP {status}"


def _credit_usage(usage: Any) -> int | float | None:
    if isinstance(usage, dict):
        credits = usage.get("credits", usage.get("credit_usage"))
        if isinstance(credits, (int, float)) and not isinstance(credits, bool):
            return credits
    return None
