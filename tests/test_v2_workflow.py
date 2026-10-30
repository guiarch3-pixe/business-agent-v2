import asyncio
import json

import pytest
from pydantic import ValidationError

from enterprise_agent.demo import (DemoEmbedder, DemoReranker, DemoLLM, DemoSearch, DemoReader, NOTE, run_demo)
from enterprise_agent.engine import ResearchEngine
from enterprise_agent.providers.base import ModelResponse, TokenUsage
from enterprise_agent.rag import KnowledgeBase, make_source
from enterprise_agent.schema import ResearchState, Plan, Coverage, Extraction, Assessment, Citation, Claim
from enterprise_agent.settings import Limits
from enterprise_agent.tools.base import ToolResult


def fixture_engine(tmp_path, llm=None, search=None, reader=None, limits=None, seed=True):
    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    if seed:
        kb.add(make_source("示例科技", "https://example.invalid/revenue", "合成材料", NOTE, kind="demo"))
    return ResearchEngine(llm or DemoLLM(), kb, search or DemoSearch(), reader or DemoReader(), limits=limits)


def execute(engine, tmp_path):
    return asyncio.run(engine.run("示例科技", "收入模式和续费情况", tmp_path / "runs", mode="demo"))


def events(directory):
    return [json.loads(line) for line in (directory / "trace.jsonl").read_text().splitlines()]


def test_actual_langgraph_multiround_rag_first_and_gap_search(tmp_path):
    state, directory = asyncio.run(run_demo(tmp_path))
    assert state.rounds == 3 and state.stop_reason == "no_open_gaps"
    assert len(state.searches) == 1
    assert state.searches[0].question_id == "q2"
    assert len(state.evidence) == 2
    assert {c.kind for c in state.claims} == {"fact", "deduction", "business_judgment", "hypothesis"}
    trace = events(directory)
    nodes = [x["node"] for x in trace if x["event"] == "node_start"]
    assert nodes.count("plan") == 3 and nodes.count("search_web") == 1
    assert nodes.index("coverage") < nodes.index("search_web")
    claims = {c.id: c for c in state.claims}
    quotes = {e.id: e.quote for e in state.evidence}
    assert "92%" in quotes[claims["c2_1"].citations[0].evidence_id]
    assert len(claims["c3_1"].citations) == 2
    assert "合成" in (directory / "report.md").read_text()
    # The saved artifact is independently reloadable and validates every span/reference.
    loaded = ResearchState.model_validate_json((directory / "state.json").read_text())
    web_evidence = next(e for e in loaded.evidence if "92%" in e.quote)
    source = next(s for s in loaded.sources if s.id == web_evidence.source_id)
    assert source.acquisition.search_id == loaded.searches[0].id
    assert source.id in loaded.searches[0].source_ids
    assert source.text[web_evidence.start:web_evidence.end] == web_evidence.quote


def test_local_coverage_avoids_all_search_in_first_round(tmp_path):
    class NoSearch:
        async def execute(self, query):
            raise AssertionError("unnecessary paid search")
    engine = fixture_engine(tmp_path, search=NoSearch(), limits=Limits(rounds=1))
    state, _ = execute(engine, tmp_path)
    assert state.claims and engine.counts["searches"] == 0
    assert state.stop_reason == "round_limit"
    assert any(g.status == "open" for g in state.gaps)


def test_fabricated_quote_rejected_atomically(tmp_path):
    class BadQuote(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Extraction:
                result.output.quotes[0].quote = "THIS WAS NEVER IN THE SOURCE"
            return result
    state, directory = execute(fixture_engine(tmp_path, llm=BadQuote()), tmp_path)
    assert state.stop_reason == "error" and not state.evidence and not state.claims
    assert events(directory)[-1]["event"] == "run_end"


def test_dangling_claim_citation_preserves_committed_evidence(tmp_path):
    class BadCitation(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Assessment:
                result.output.claims[0].citations = [Citation(evidence_id="not-found", relation="supports")]
            return result
    state, directory = execute(fixture_engine(tmp_path, llm=BadCitation()), tmp_path)
    assert state.stop_reason == "error" and len(state.evidence) == 1 and not state.claims
    saved = ResearchState.model_validate_json((directory / "state.json").read_text())
    assert saved.evidence and saved.gaps[0].status == "open"


def test_empty_synthesis_fails_and_keeps_evidence(tmp_path):
    class Empty(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            if schema is Assessment:
                return ModelResponse(output=Assessment(claims=[], rationale="空内容"), model="fake", usage=TokenUsage())
            return await super().generate(prompt, schema, **kwargs)
    state, _ = execute(fixture_engine(tmp_path, llm=Empty()), tmp_path)
    assert state.stop_reason == "error" and state.evidence and not state.claims


def test_planner_cannot_target_an_invented_gap(tmp_path):
    class BadPlan(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Plan:
                result.output.gap_id = "invented"
            return result
    engine = fixture_engine(tmp_path, llm=BadPlan())
    state, _ = execute(engine, tmp_path)
    assert state.stop_reason == "error" and engine.counts["searches"] == 0


def test_coverage_cannot_cite_nonexistent_chunks(tmp_path):
    class BadCoverage(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Coverage:
                result.output.chunk_ids = ["invented"]
            return result
    state, _ = execute(fixture_engine(tmp_path, llm=BadCoverage()), tmp_path)
    assert state.stop_reason == "error" and not state.evidence


def test_search_snippet_is_never_page_evidence(tmp_path):
    class FailedReader:
        async def execute(self, url):
            return ToolResult(tool_name="read", query_or_input=url)
    engine = fixture_engine(tmp_path, reader=FailedReader(), seed=False, limits=Limits(rounds=2, no_progress_rounds=1))
    state, _ = execute(engine, tmp_path)
    assert not state.evidence and not state.claims
    assert state.gaps[0].status == "open"
    assert engine.counts["searches"] == 1  # Duplicate queries do not spend twice.
    assert state.stop_reason == "no_progress"


def test_budget_is_shared_across_nodes_and_keeps_previous_results(tmp_path):
    engine = fixture_engine(tmp_path, limits=Limits(model_calls=3))
    state, _ = execute(engine, tmp_path)
    assert state.stop_reason == "budget_model_calls"
    assert engine.counts["model_calls"] == 3
    assert state.evidence and not state.claims


def test_timeout_preserves_checkpoint(tmp_path):
    class Slow(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            if schema is Assessment:
                await asyncio.sleep(2)
            return await super().generate(prompt, schema, **kwargs)
    state, directory = execute(fixture_engine(tmp_path, llm=Slow(), limits=Limits(timeout=.5)), tmp_path)
    assert state.stop_reason == "timeout" and state.evidence
    assert (directory / "report.md").exists()


def test_cancel_writes_terminal_artifacts(tmp_path):
    entered = asyncio.Event()
    class Slow(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            entered.set()
            await asyncio.sleep(10)
    engine = fixture_engine(tmp_path, llm=Slow())
    async def run():
        task = asyncio.create_task(engine.run("示例科技", "问题", tmp_path / "runs"))
        await entered.wait()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
    asyncio.run(run())
    directory = next((tmp_path / "runs").iterdir())
    saved = ResearchState.model_validate_json((directory / "state.json").read_text())
    assert saved.stop_reason == "cancelled"


@pytest.mark.parametrize("mutation", ["quote", "hash", "chunk", "citation", "duplicate", "resolved_hypothesis", "cross_gap"])
def test_pydantic_rejects_tampered_saved_provenance(tmp_path, mutation):
    state, _ = asyncio.run(run_demo(tmp_path))
    data = state.model_dump()
    if mutation == "quote":
        data["evidence"][0]["quote"] = "伪造原文"
    elif mutation == "hash":
        data["sources"][0]["text"] = "改写原始文本"
    elif mutation == "chunk":
        data["chunks"][0]["start"] += 1
    elif mutation == "citation":
        data["claims"][0]["citations"][0]["evidence_id"] = "unknown"
    elif mutation == "duplicate":
        data["evidence"].append(data["evidence"][0])
    elif mutation == "resolved_hypothesis":
        data["gaps"][0]["resolution_claim_ids"] = ["c1_4"]
    elif mutation == "cross_gap":
        data["gaps"][0]["resolution_claim_ids"] = ["c2_1"]
    with pytest.raises(ValidationError):
        ResearchState.model_validate(data)


def test_fact_cannot_be_supported_without_evidence():
    with pytest.raises(ValidationError):
        Claim(id="c", question_id="q", kind="fact", text="断言", status="supported", rationale="无依据")


def test_conflicting_evidence_must_not_be_labelled_supported():
    with pytest.raises(ValidationError):
        Claim(id="c", question_id="q", kind="fact", text="断言", status="supported", rationale="矛盾",
              citations=[Citation(evidence_id="e1", relation="supports"), Citation(evidence_id="e2", relation="contradicts")])
