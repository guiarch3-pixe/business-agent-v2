"""Mocked-HTTP tests for the Tavily search adapter.

No test reaches the network and no test holds a real search credential.
"""

from __future__ import annotations

import asyncio
import json
from datetime import timezone

import httpx
import pytest

from enterprise_agent.tools.tavily import TavilySearchTool

SECRET = "tvly-unit-test-secret-value"
SEARCH_URL = "https://api.tavily.com/search"


def _client(handler) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def _tool(handler, **kwargs) -> TavilySearchTool:
    return TavilySearchTool(api_key=SECRET, client=_client(handler), **kwargs)


def _payload(results, usage=None):
    body = {"query": "q", "results": results}
    if usage is not None:
        body["usage"] = usage
    return body


def _result(url="https://example.invalid/a", title="A page", content="snippet text"):
    return {"url": url, "title": title, "content": content, "score": 0.9}


def test_request_shape_and_auth_placement():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json=_payload([_result()]))

    result = asyncio.run(_tool(handler).execute("accreditation value"))

    request = captured["request"]
    assert request.method == "POST"
    assert str(request.url) == SEARCH_URL
    assert request.headers["authorization"] == f"Bearer {SECRET}"

    body = json.loads(request.content)
    assert body["query"] == "accreditation value"
    assert body["search_depth"] == "basic"
    assert body["max_results"] == 3
    assert body["include_answer"] is False
    assert body["include_raw_content"] is False
    assert body["include_usage"] is True

    assert result.tool_name == "search_web"
    assert result.query_or_input == "accreditation value"
    assert result.error is None


def test_results_become_records_with_snippet_provenance():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json=_payload(
                [
                    _result("https://a.invalid/one", "First", "first snippet"),
                    _result("https://b.invalid/two", "Second", "second snippet"),
                ]
            ),
        )

    result = asyncio.run(_tool(handler, max_results=2).execute("q"))

    assert [record.source_url for record in result.records] == ["https://a.invalid/one", "https://b.invalid/two"]
    assert [record.content for record in result.records] == ["first snippet", "second snippet"]
    assert [record.source_title for record in result.records] == ["First", "Second"]
    for record in result.records:
        assert record.retrieved_at.tzinfo is not None
        assert record.retrieved_at.utcoffset() == timezone.utc.utcoffset(None)
        assert "snippet" in record.source_location
        assert "not page text" in record.source_location


def test_credit_usage_and_call_count_are_reported():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=_payload([_result()], usage={"credits": 1}))

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.cost_metadata["search_calls"] == 1
    assert result.cost_metadata["credits"] == 1
    assert result.cost_metadata["provider"] == "tavily"


def test_missing_credit_usage_is_not_invented():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=_payload([_result()]))

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.cost_metadata["search_calls"] == 1
    assert result.cost_metadata["credits"] is None


def test_no_results_is_a_success_not_an_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=_payload([]))

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.records == []
    assert result.error is None
    assert result.cost_metadata["search_calls"] == 1


@pytest.mark.parametrize(
    ("status", "code"),
    [(401, "auth_error"), (403, "auth_error"), (429, "rate_limited"), (500, "server_error"), (400, "http_error")],
)
def test_provider_failures_map_to_normalized_errors(status, code):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(status, json={"detail": f"echo {SECRET}"})

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.error is not None
    assert result.error.code == code
    assert result.records == []
    assert len(calls) == 1
    assert SECRET not in result.error.message
    assert "echo" not in result.error.message


def test_timeout_and_connection_failure_are_normalized():
    def timing_out(request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("slow", request=request)

    def refusing(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)

    timeout = asyncio.run(_tool(timing_out).execute("q"))
    assert timeout.error is not None and timeout.error.code == "timeout"
    assert timeout.records == []

    network = asyncio.run(_tool(refusing).execute("q"))
    assert network.error is not None and network.error.code == "network_error"


def test_unparseable_body_is_an_error_not_an_empty_search():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "text/html"}, content=b"<html>captcha</html>")

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.error is not None
    assert result.error.code == "invalid_response"
    assert result.records == []


@pytest.mark.parametrize(
    "results",
    [
        "not-a-list",
        [{"title": "no url", "content": "c"}],
        [{"url": "https://a.invalid/x", "content": "c"}],
        [{"url": "https://a.invalid/x", "title": "t"}],
        [{"url": "https://a.invalid/x", "title": "t", "content": "   "}],
        [{"url": "not-a-url", "title": "t", "content": "c"}],
        [{"url": "https://a.invalid/x", "title": "t", "content": "c"}, {"url": "https://a.invalid/x"}],
    ],
)
def test_malformed_results_are_explicit_provider_errors(results):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=_payload(results))

    result = asyncio.run(_tool(handler).execute("q"))
    assert result.error is not None, results
    assert result.error.code == "invalid_response"
    assert result.records == []


def test_blank_query_and_invalid_limits_are_rejected_before_any_call():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json=_payload([_result()]))

    tool = _tool(handler)
    with pytest.raises(ValueError):
        asyncio.run(tool.execute("   "))
    with pytest.raises(ValueError):
        TavilySearchTool(api_key="  ", client=_client(handler))
    with pytest.raises(ValueError):
        TavilySearchTool(api_key=SECRET, max_results=0, client=_client(handler))
    with pytest.raises(ValueError):
        TavilySearchTool(api_key=SECRET, max_results=100, client=_client(handler))
    with pytest.raises(ValueError):
        TavilySearchTool(api_key=SECRET, timeout=0, client=_client(handler))
    assert calls == []


def test_tool_name_is_the_shared_contract_name():
    assert TavilySearchTool.name == "search_web"
