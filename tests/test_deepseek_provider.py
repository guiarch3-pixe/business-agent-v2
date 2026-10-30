"""Mocked-HTTP tests for the DeepSeek structured-output adapter.

Every test injects an ``httpx.MockTransport`` client; no test opens a socket and
no test holds a real credential.
"""

from __future__ import annotations

import asyncio
import json

import httpx
import pytest
from pydantic import BaseModel, ConfigDict

from enterprise_agent.providers.deepseek import DeepSeekLLM
from enterprise_agent.providers.errors import ModelCallError

SECRET = "sk-unit-test-secret-value"

CHAT_URL = "https://api.deepseek.com/chat/completions"


class Plan(BaseModel):
    model_config = ConfigDict(extra="forbid")

    query: str


def _client(handler) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def _completion(content: str, *, model: str = "deepseek-flash-2026", finish: str = "stop", usage=None):
    body = {
        "id": "cmpl-1",
        "model": model,
        "choices": [{"index": 0, "finish_reason": finish, "message": {"role": "assistant", "content": content}}],
    }
    if usage is not None:
        body["usage"] = usage
    return httpx.Response(200, json=body)


def _llm(handler, **kwargs) -> DeepSeekLLM:
    return DeepSeekLLM(api_key=SECRET, client=_client(handler), **kwargs)


def test_request_shape_carries_auth_model_and_json_mode():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return _completion(json.dumps({"query": "accreditation value chain"}))

    llm = _llm(handler, model="deepseek-flash", max_output_tokens=1234)
    response = asyncio.run(llm.generate("plan a search", Plan))

    request = captured["request"]
    assert request.method == "POST"
    assert str(request.url) == CHAT_URL
    assert request.headers["authorization"] == f"Bearer {SECRET}"

    body = json.loads(request.content)
    assert body["model"] == "deepseek-flash"
    assert body["stream"] is False
    assert body["max_tokens"] == 1234
    assert body["response_format"] == {"type": "json_object"}
    assert body["thinking"] == {"type": "disabled"}
    assert [message["role"] for message in body["messages"]] == ["system", "user"]
    assert body["messages"][1]["content"] == "plan a search"
    system = body["messages"][0]["content"]
    assert "JSON" in system
    assert "query" in system  # the schema is handed to the model
    assert response.output.query == "accreditation value chain"


def test_actual_returned_model_and_token_usage_are_preserved():
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(
            json.dumps({"query": "q"}),
            model="deepseek-flash-returned",
            usage={"prompt_tokens": 11, "completion_tokens": 7, "total_tokens": 18},
        )

    response = asyncio.run(_llm(handler).generate("prompt", Plan))
    assert response.model == "deepseek-flash-returned"
    assert response.usage.input_tokens == 11
    assert response.usage.output_tokens == 7


def test_missing_usage_stays_unknown_not_zero():
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"query": "q"}))

    response = asyncio.run(_llm(handler).generate("prompt", Plan))
    assert response.usage.input_tokens is None
    assert response.usage.output_tokens is None


def test_partial_usage_keeps_the_missing_half_unknown():
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"query": "q"}), usage={"completion_tokens": 4})

    response = asyncio.run(_llm(handler).generate("prompt", Plan))
    assert response.usage.input_tokens is None
    assert response.usage.output_tokens == 4


@pytest.mark.parametrize(
    ("content", "finish"),
    [("", "stop"), ("   ", "stop"), (json.dumps({"query": "q"}), "length")],
)
def test_empty_or_unfinished_output_is_rejected(content, finish):
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(content, finish=finish)

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code in {"empty_output", "truncated_output"}


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        ("not json at all", "invalid_json"),
        ('{"query": "q", "unexpected": 1}', "invalid_schema"),
        ('{"not_query": "q"}', "invalid_schema"),
        ('{"query": 17}', "invalid_schema"),
    ],
)
def test_malformed_or_off_schema_json_is_rejected(content, expected):
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(content)

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == expected


def test_json_array_output_is_rejected():
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion("[1, 2, 3]")

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == "invalid_json"


def test_response_body_that_is_not_json_is_rejected():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, headers={"content-type": "text/html"}, content=b"<html>nope</html>")

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == "invalid_response"


@pytest.mark.parametrize(
    ("status", "code"),
    [(401, "auth_error"), (403, "auth_error"), (429, "rate_limited"), (500, "server_error"), (503, "server_error"), (400, "http_error")],
)
def test_http_failures_map_to_stable_codes_without_retry(status, code):
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(status, json={"error": {"message": f"provider detail {SECRET}"}})

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == code
    assert len(calls) == 1, "no automatic retry"
    assert SECRET not in str(error.value)
    assert "provider detail" not in str(error.value)


def test_timeout_and_connection_errors_are_typed():
    def timing_out(request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("too slow", request=request)

    def refusing(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("no route", request=request)

    with pytest.raises(ModelCallError) as timeout_error:
        asyncio.run(_llm(timing_out).generate("prompt", Plan))
    assert timeout_error.value.code == "timeout"

    with pytest.raises(ModelCallError) as network_error:
        asyncio.run(_llm(refusing).generate("prompt", Plan))
    assert network_error.value.code == "network_error"


def test_choices_payload_without_a_message_is_rejected():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"model": "m", "choices": []})

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == "empty_output"


def test_a_schema_failure_keeps_reported_usage_and_records_only_locations():
    """A billed response that fails validation still spent tokens, and must say where."""

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(
            json.dumps({"query": "q", "unexpected": "sk-should-not-be-recorded"}),
            usage={"prompt_tokens": 1500, "completion_tokens": 200},
        )

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))

    assert error.value.code == "invalid_schema"
    assert error.value.usage is not None
    assert error.value.usage.input_tokens == 1500
    assert error.value.usage.output_tokens == 200
    # Location and kind only: the offending value, the raw body and any reasoning stay out.
    # The unknown field name is model-authored, so it is masked rather than echoed.
    assert error.value.schema_errors
    joined = " ".join(error.value.schema_errors)
    assert "extra_forbidden" in joined
    assert "unexpected" not in joined
    assert "sk-should-not-be-recorded" not in str(error.value)
    assert "sk-should-not-be-recorded" not in joined


def test_json_failure_also_keeps_reported_usage():
    def handler(request: httpx.Request) -> httpx.Response:
        return _completion("not json at all", usage={"prompt_tokens": 42, "completion_tokens": 3})

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.code == "invalid_json"
    assert error.value.usage.input_tokens == 42
    assert error.value.usage.output_tokens == 3


def test_an_http_failure_reports_no_usage_because_none_was_returned():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, json={"error": {"message": "slow down"}})

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Plan))
    assert error.value.usage is None


def test_untrusted_extra_field_names_do_not_reach_the_diagnostics():
    """An unknown key is model-controlled text, so it must not be echoed as a path."""

    class Narrow(BaseModel):
        model_config = ConfigDict(extra="forbid")
        query: str

    sentinel = "SECRET-SENTINEL" + "A" * 2000

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"query": "q", sentinel: "x"}))

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Narrow))

    joined = " ".join(error.value.schema_errors)
    assert "SECRET-SENTINEL" not in joined
    assert "AAAA" not in joined
    assert all(len(location) <= 120 for location in error.value.schema_errors)


def test_unknown_keys_are_replaced_with_a_placeholder_but_known_paths_survive():
    class Narrow(BaseModel):
        model_config = ConfigDict(extra="forbid")
        query: str
        n: int

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"query": "q", "n": 1, "some_model_key": 2}))

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Narrow))

    joined = " ".join(error.value.schema_errors)
    assert "some_model_key" not in joined
    assert "extra_forbidden" in joined


def test_a_known_schema_path_is_still_reported_usefully():
    """The fix must not blunt the diagnostics that made this worth having."""

    class Nested(BaseModel):
        model_config = ConfigDict(extra="forbid")
        claims: list[Plan]

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"claims": [{"query": 17}]}))

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Nested))

    joined = " ".join(error.value.schema_errors)
    assert "claims.0.query" in joined
    assert "string_type" in joined


def test_a_dynamic_mapping_key_is_replaced_with_a_bounded_index():
    class Dynamic(BaseModel):
        model_config = ConfigDict(extra="forbid")
        lookup: dict[str, int]

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"lookup": {"model-supplied-KEY": "not-an-int"}}))

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Dynamic))

    joined = " ".join(error.value.schema_errors)
    assert "model-supplied-KEY" not in joined
    assert "lookup" in joined


def test_schema_error_locations_are_capped():
    class Wide(BaseModel):
        model_config = ConfigDict(extra="forbid")
        a: int
        b: int
        c: int

    def handler(request: httpx.Request) -> httpx.Response:
        return _completion(json.dumps({"a": "x", "b": "y", "c": "z", "d": 1, "e": 2}))

    with pytest.raises(ModelCallError) as error:
        asyncio.run(_llm(handler).generate("prompt", Wide))
    assert 0 < len(error.value.schema_errors) <= 10


def test_the_configured_model_is_exposed_for_labelling_a_failed_attempt():
    assert _llm(lambda request: _completion(json.dumps({"query": "q"})), model="deepseek-x").model == "deepseek-x"


def test_base_url_trailing_slash_is_normalised():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return _completion(json.dumps({"query": "q"}))

    asyncio.run(_llm(handler, base_url="https://api.deepseek.com/").generate("prompt", Plan))
    assert seen["url"] == CHAT_URL


def test_blank_api_key_and_invalid_limits_are_rejected_before_any_call():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return _completion(json.dumps({"query": "q"}))

    with pytest.raises(ValueError):
        DeepSeekLLM(api_key="   ", client=_client(handler))
    with pytest.raises(ValueError):
        DeepSeekLLM(api_key=SECRET, max_output_tokens=0, client=_client(handler))
    with pytest.raises(ValueError):
        DeepSeekLLM(api_key=SECRET, timeout=0, client=_client(handler))
    assert calls == []
