"""Offline adversarial checks for V2: routing, retrieval boundaries, contracts.

Every test here uses the synthetic demo fixtures or mocked HTTP transports. No
test reads ``.env``, opens a socket or calls a paid API.
"""
from __future__ import annotations

import asyncio
import copy
import json
from pathlib import Path

import httpx
import numpy as np
import pytest
from pydantic import ValidationError

from enterprise_agent.demo import (
    COMPANY,
    DemoEmbedder,
    DemoLLM,
    DemoReader,
    DemoReranker,
    DemoSearch,
    GOAL,
    NOTE,
    run_demo,
)
from enterprise_agent.engine import ResearchEngine
from enterprise_agent.providers.base import ModelResponse, TokenUsage
from enterprise_agent.providers.dashscope import DashScopeEmbedder, RetrievalAPIError
from enterprise_agent.providers.errors import ModelCallError
from enterprise_agent.rag import KnowledgeBase, make_source
from enterprise_agent.schema import Coverage, Plan, ResearchState
from enterprise_agent.settings import Limits


# --------------------------------------------------------------- test helpers


def build_engine(tmp_path, *, kb=None, llm=None, search=None, reader=None, limits=None, seed=True):
    kb = kb or KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    if seed:
        kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成年度订阅资料", NOTE, kind="demo"))
    return ResearchEngine(llm or DemoLLM(), kb, search or DemoSearch(), reader or DemoReader(), limits=limits)


def run_engine(engine, tmp_path):
    return asyncio.run(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))


def trace(directory: Path):
    return [json.loads(line) for line in (directory / "trace.jsonl").read_text().splitlines()]


def saved_state(directory: Path) -> ResearchState:
    return ResearchState.model_validate_json((directory / "state.json").read_text())


def payload_of(prompt: str):
    return json.loads(prompt.split("DATA:\n", 1)[1])


class ForceRetentionSearch(DemoLLM):
    """Ask for retention in round one and declare the local corpus insufficient."""

    async def generate(self, prompt, schema, **kwargs):
        data = payload_of(prompt)
        if schema is Plan and not data["claims"]:
            return ModelResponse(
                output=Plan(gap_id="gap0", question="示例科技客户续费率是多少？",
                            query="示例科技 客户续费率", rationale="先查续费证据"),
                model="synthetic-plan", usage=TokenUsage(),
            )
        if schema is Coverage:
            return ModelResponse(
                output=Coverage(sufficient=False, chunk_ids=[], rationale="缺少续费率证据", missing="客户续费率"),
                model="synthetic-coverage", usage=TokenUsage(),
            )
        return await super().generate(prompt, schema, **kwargs)


# ------------------------------------------------------- LangGraph gap routing


def test_unresolved_gaps_drive_rounds_and_a_resolved_gap_is_not_replanned(tmp_path):
    state, directory = asyncio.run(run_demo(tmp_path))
    plans = [event["plan"]["gap_id"] for event in trace(directory) if event["event"] == "question"]
    assert plans == ["gap0", "gap1", "gap0"]
    assert state.stop_reason == "no_open_gaps"
    assert state.questions[2].parent_gap_id == state.gaps[1].id

    class TargetsResolvedGap(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Plan:
                data = payload_of(prompt)
                if any(claim["id"].startswith("c2_") for claim in data["claims"]):
                    result.output.gap_id = "gap1"
            return result

    engine = build_engine(tmp_path / "replan", llm=TargetsResolvedGap())
    state, directory = run_engine(engine, tmp_path / "replan")
    assert state.stop_reason == "error"
    assert state.rounds == 2
    assert next(g for g in state.gaps if g.id == "gap1").status == "resolved"
    assert next(g for g in state.gaps if g.id == "gap0").status == "open"
    assert len(state.evidence) == 2 and len(state.claims) == 5
    assert saved_state(directory).stop_reason == "error"


def test_sufficient_local_coverage_does_not_search(tmp_path):
    class NoSearch:
        async def execute(self, query):
            raise AssertionError("search must not be called when coverage is sufficient")

    engine = build_engine(tmp_path, search=NoSearch(), limits=Limits(rounds=1))
    state, _ = run_engine(engine, tmp_path)
    assert engine.counts["searches"] == 0
    assert state.claims and state.evidence
    assert state.stop_reason == "round_limit" and any(g.status == "open" for g in state.gaps)


def test_initial_source_url_gets_current_run_provenance(tmp_path):
    engine = build_engine(tmp_path, seed=False, limits=Limits(rounds=1))
    state, directory = asyncio.run(engine.run(
        COMPANY, GOAL, tmp_path / "runs", mode="demo",
        source_urls=["https://example.invalid/initial"],
    ))
    source = next(item for item in state.sources if item.url.endswith("/initial"))
    assert source.acquisition.run_id == state.run_id
    assert source.acquisition.question_id == "q0"
    assert source.acquisition.search_id is None
    assert saved_state(directory).sources


def test_insufficient_coverage_searches_reads_reindexes_and_extracts(tmp_path):
    engine = build_engine(tmp_path, llm=ForceRetentionSearch(), limits=Limits(rounds=1))
    state, directory = run_engine(engine, tmp_path)

    assert engine.counts["searches"] == 1 and engine.counts["pages"] == 1
    events = trace(directory)
    nodes = [event["node"] for event in events if event["event"] == "node_start"]
    assert nodes.index("coverage") < nodes.index("search_web") < nodes.index("retrieve_external")
    assert nodes.index("retrieve_external") < nodes.index("extract")

    retrievals = [event for event in events if event["event"] == "retrieval"]
    assert len(retrievals) == 2
    web_source = next(source for source in state.sources if source.url.endswith("/retention"))
    assert web_source.id in {hit["source_id"] for hit in retrievals[1]["hits"]}
    assert any("92%" in evidence.quote for evidence in state.evidence)
    assert state.stop_reason == "round_limit"


# ------------------------------------------------------- retrieval boundaries


def test_rerank_scores_stay_attached_to_the_same_dense_candidates(tmp_path):
    dense = {"alpha": 0.9, "beta": 0.4, "gamma": 0.1}
    expected_rerank = {"alpha": 1.0, "beta": 9.0, "gamma": 5.0}

    class ControlledEmbedder:
        name = "controlled-embedder"

        def encode(self, texts, *, text_type="document"):
            if text_type == "query":
                return np.array([[1.0, 0.0]])
            return np.array([[dense[text], 1.0] for text in texts])

    class ControlledReranker:
        name = "controlled-reranker"

        def score(self, query, documents):
            return [expected_rerank[document] for document in documents]

    kb = KnowledgeBase(tmp_path / "kb.db", ControlledEmbedder(), ControlledReranker())
    for text in dense:
        kb.add(make_source("排序企业", f"https://example.invalid/{text}", text, text, kind="web"))

    hits = kb.retrieve("排序企业", "query", candidates=3, top_k=3)
    assert [hit.chunk.text for hit in hits] == ["beta", "gamma", "alpha"]
    for hit in hits:
        norm = float(np.hypot(dense[hit.chunk.text], 1.0))
        assert hit.vector_score == pytest.approx(dense[hit.chunk.text] / norm)
        assert hit.rerank_score == expected_rerank[hit.chunk.text]


@pytest.mark.parametrize(
    "vectors",
    [
        np.array([[1.0, 2.0], [3.0, 4.0]]),       # wrong count
        np.array([1.0, 2.0]),                     # wrong rank
        np.array([[float("nan"), 2.0]]),          # non-finite
        np.array([[0.0, 0.0]]),                   # zero vector
        np.array([[True, False]]),                # bools are not numbers
        np.array([["1.0", "2.0"]]),               # numeric strings are not vectors
    ],
)
def test_invalid_embedding_response_is_rejected_without_partial_writes(tmp_path, vectors):
    class BadEmbedder:
        name = "bad-embedder"

        def encode(self, texts, *, text_type="document"):
            return vectors

    kb = KnowledgeBase(tmp_path / "kb.db", BadEmbedder(), DemoReranker())
    with pytest.raises(ValueError):
        kb.add(make_source("企业", "https://example.invalid/a", "标题", "正文", kind="web"))
    with kb.connect() as db:
        assert db.execute("SELECT count(*) FROM sources").fetchone()[0] == 0
        assert db.execute("SELECT count(*) FROM chunks").fetchone()[0] == 0


def test_invalid_query_embedding_and_reranker_responses_are_rejected(tmp_path):
    class BadQueryEmbedder:
        name = "bad-query"

        def encode(self, texts, *, text_type="document"):
            if text_type == "query":
                return np.ones((2, 2))
            return np.ones((len(texts), 2))

    kb = KnowledgeBase(tmp_path / "bad-query.db", BadQueryEmbedder(), DemoReranker())
    kb.add(make_source("企业", "https://example.invalid/a", "标题", "正文", kind="web"))
    with pytest.raises(ValueError):
        kb.retrieve("企业", "query")

    class FlatEmbedder:
        name = "flat"

        def encode(self, texts, *, text_type="document"):
            return np.ones((len(texts), 2))

    for index, scores in enumerate(([0.5], [0.5, float("nan")], [0.5, 0.4, 0.3])):
        class FixedReranker:
            name = "fixed"

            def score(self, query, documents):
                return scores

        db = tmp_path / f"rerank-{index}.db"
        bad = KnowledgeBase(db, FlatEmbedder(), FixedReranker())
        for source_index in range(2):
            bad.add(make_source("企业", f"https://example.invalid/{source_index}",
                                "标题", f"正文{source_index}", kind="web"))
        with pytest.raises(ValueError):
            bad.retrieve("企业", "query", candidates=2, top_k=1)


def test_empty_company_scope_spends_no_embedding_or_rerank_call(tmp_path):
    class CountingEmbedder:
        name = "counting"
        calls = 0

        def encode(self, texts, *, text_type="document"):
            CountingEmbedder.calls += 1
            return np.ones((len(texts), 2))

    class CountingReranker:
        name = "counting-rerank"
        calls = 0

        def score(self, query, documents):
            CountingReranker.calls += 1
            return [0.0] * len(documents)

    kb = KnowledgeBase(tmp_path / "kb.db", CountingEmbedder(), CountingReranker())
    assert kb.retrieve("不存在的企业", "query") == []
    assert CountingEmbedder.calls == 0 and CountingReranker.calls == 0


def test_identical_text_is_isolated_by_company(tmp_path):
    class ConstantEmbedder:
        name = "constant"

        def encode(self, texts, *, text_type="document"):
            return np.ones((len(texts), 2))

    class ConstantReranker:
        name = "constant-rerank"

        def score(self, query, documents):
            return [1.0] * len(documents)

    kb = KnowledgeBase(tmp_path / "kb.db", ConstantEmbedder(), ConstantReranker())
    text = "两家公司拥有完全相同的正文"
    kb.add(make_source("甲企业", "https://example.invalid/shared", "标题", text, kind="web"))
    kb.add(make_source("乙企业", "https://example.invalid/shared", "标题", text, kind="web"))

    assert {hit.source.company for hit in kb.retrieve("甲企业", text)} == {"甲企业"}
    assert {hit.source.company for hit in kb.retrieve("乙企业", text)} == {"乙企业"}


def test_embedding_dimension_change_is_rejected_before_writing(tmp_path):
    class FixedDimension:
        name = "same-name"

        def __init__(self, dimension):
            self.dimension = dimension

        def encode(self, texts, *, text_type="document"):
            return np.ones((len(texts), self.dimension))

    class FlatReranker:
        name = "flat"

        def score(self, query, documents):
            return [0.0] * len(documents)

    kb = KnowledgeBase(tmp_path / "kb.db", FixedDimension(2), FlatReranker())
    kb.add(make_source("企业", "https://example.invalid/a", "标题", "正文", kind="web"))
    reopened = KnowledgeBase(tmp_path / "kb.db", FixedDimension(3), FlatReranker())
    with pytest.raises(ValueError, match="dimension"):
        reopened.add(make_source("企业", "https://example.invalid/b", "标题", "另一段正文", kind="web"))


def test_source_reused_from_an_earlier_run_keeps_historical_acquisition(tmp_path):
    first_kb = KnowledgeBase(tmp_path / "shared.db", DemoEmbedder(), DemoReranker())
    first = build_engine(tmp_path / "run1", kb=first_kb, llm=ForceRetentionSearch(), limits=Limits(rounds=1))
    first_state, _ = run_engine(first, tmp_path / "run1")
    web_source = next(source for source in first_state.sources if source.url.endswith("/retention"))
    assert web_source.acquisition.run_id == first_state.run_id

    class RetentionPlan(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            if schema is Plan and not payload_of(prompt)["claims"]:
                return ModelResponse(
                    output=Plan(gap_id="gap0", question="示例科技客户续费率是多少？",
                                query="示例科技 客户续费率", rationale="资料库中已有续费资料"),
                    model="synthetic-plan", usage=TokenUsage(),
                )
            return await super().generate(prompt, schema, **kwargs)

    second_kb = KnowledgeBase(tmp_path / "shared.db", DemoEmbedder(), DemoReranker())
    second = build_engine(tmp_path / "run2", kb=second_kb, llm=RetentionPlan(), limits=Limits(rounds=1))
    second_state, directory = run_engine(second, tmp_path / "run2")

    assert second.counts["searches"] == 0
    evidence = next(item for item in second_state.evidence if "92%" in item.quote)
    reused = next(source for source in second_state.sources if source.id == evidence.source_id)
    assert reused.acquisition.run_id == first_state.run_id != second_state.run_id
    assert saved_state(directory).run_id == second_state.run_id


# ----------------------------------------------------------- provider boundary


def _embedding_embedder(embedding, dimensions=64):
    payload = {"output": {"embeddings": [{"text_index": 0, "embedding": embedding}]}}
    client = httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200, json=payload)))
    return DashScopeEmbedder("test-key", "https://example.invalid/embed",
                             dimensions=dimensions, client=client)


@pytest.mark.parametrize("component", [True, "1.0"])
def test_dashscope_rejects_non_numeric_embedding_components(component):
    with pytest.raises(RetrievalAPIError):
        _embedding_embedder([1.0] * 63 + [component]).encode(["text"])


def test_dashscope_rejects_nonfinite_embedding_components():
    vector = ",".join(["1.0"] * 63) + ",NaN"
    body = ('{"output":{"embeddings":[{"text_index":0,"embedding":[' + vector + "]}]}}").encode()
    client = httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200, content=body)))
    embedder = DashScopeEmbedder("test-key", "https://example.invalid/embed", dimensions=64, client=client)
    with pytest.raises(RetrievalAPIError):
        embedder.encode(["text"])


# ------------------------------------------------------------ Pydantic gates


@pytest.fixture(scope="module")
def demo_state(tmp_path_factory):
    state, _ = asyncio.run(run_demo(tmp_path_factory.mktemp("schema-demo")))
    return state


def assert_invalid(state: ResearchState, mutate):
    data = copy.deepcopy(state.model_dump())
    mutate(data)
    with pytest.raises(ValidationError):
        ResearchState.model_validate(data)


def current_run_acquisition(data):
    return next(source["acquisition"] for source in data["sources"]
                if source.get("acquisition") and source["acquisition"]["run_id"] == data["run_id"])


@pytest.mark.parametrize("field", ["question_id", "search_id"])
def test_dangling_current_run_acquisition_reference_is_rejected(demo_state, field):
    assert_invalid(demo_state, lambda data: current_run_acquisition(data).__setitem__(field, "ghost"))


def test_current_run_acquisition_must_match_its_search_question(demo_state):
    def mutate(data):
        current_run_acquisition(data)["question_id"] = "q3"

    assert_invalid(demo_state, mutate)


def test_current_run_acquisition_source_must_be_on_its_search(demo_state):
    def mutate(data):
        data["searches"][0]["source_ids"] = []

    assert_invalid(demo_state, mutate)


@pytest.mark.parametrize("field,value", [("question_id", "q0"), ("gap_id", "gap0")])
def test_search_record_question_and_gap_anchor_must_agree(demo_state, field, value):
    def mutate(data):
        data["searches"][0][field] = value

    assert_invalid(demo_state, mutate)


def test_resolved_gap_needs_a_nonblank_rationale(demo_state):
    def mutate(data):
        gap = next(item for item in data["gaps"] if item["status"] == "resolved")
        gap["resolution_reason"] = "   "

    assert_invalid(demo_state, mutate)


def test_resolved_gap_rejects_duplicate_resolution_claims(demo_state):
    def mutate(data):
        gap = next(item for item in data["gaps"] if item["status"] == "resolved")
        gap["resolution_claim_ids"] = gap["resolution_claim_ids"] * 2

    assert_invalid(demo_state, mutate)


def test_foreign_run_acquisition_is_historical_not_dangling(demo_state):
    """A source reused from an older run keeps that run id and still validates."""

    data = copy.deepcopy(demo_state.model_dump())
    current_run_acquisition(data)["run_id"] = "previous-run"
    ResearchState.model_validate(data)


# ------------------------------------ preservation on failure/budget/cancel


def test_failure_in_second_round_keeps_first_round_evidence_and_open_gap(tmp_path):
    class FailsSecondCoverage(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            if schema is Coverage and payload_of(prompt)["gap"]["id"] == "gap1":
                raise ModelCallError("server_error", "synthetic failure")
            return await super().generate(prompt, schema, **kwargs)

    engine = build_engine(tmp_path, llm=FailsSecondCoverage())
    state, directory = run_engine(engine, tmp_path)

    assert state.stop_reason == "error"
    assert len(state.evidence) == 1 and len(state.claims) == 4
    assert next(gap for gap in state.gaps if gap.id == "gap1").status == "open"
    assert (directory / "report.md").exists()
    assert saved_state(directory).stop_reason == "error"


def test_exhausted_search_budget_keeps_local_findings_and_open_gap(tmp_path):
    engine = build_engine(tmp_path, llm=ForceRetentionSearch(), limits=Limits(rounds=1, searches=0))
    state, _ = run_engine(engine, tmp_path)

    assert engine.counts["searches"] == 0
    assert state.stop_reason == "round_limit"
    assert state.evidence and state.claims
    assert any(gap.status == "open" for gap in state.gaps)


def test_cancellation_during_search_keeps_verified_round_and_search_record(tmp_path):
    class HangingSearch:
        def __init__(self):
            self.entered = asyncio.Event()

        async def execute(self, query):
            self.entered.set()
            await asyncio.sleep(30)

    search = HangingSearch()
    engine = build_engine(tmp_path, search=search)

    async def cancel_run():
        task = asyncio.create_task(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))
        await asyncio.wait_for(search.entered.wait(), timeout=2)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(cancel_run())
    directory = next((tmp_path / "runs").iterdir())
    state = saved_state(directory)
    assert state.stop_reason == "cancelled"
    assert len(state.evidence) == 1 and len(state.claims) == 4
    assert len(state.searches) == 1
    assert (directory / "report.md").exists()
