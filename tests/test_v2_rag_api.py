import json
from pathlib import Path

import httpx
import numpy as np
import pytest

from enterprise_agent.demo import DemoEmbedder, DemoReranker
from enterprise_agent.providers.dashscope import DashScopeEmbedder, DashScopeReranker, RetrievalAPIError
from enterprise_agent.rag import KnowledgeBase, clean_text, make_source, split_source


def test_dashscope_embedding_batches_indices_and_query_type():
    requests = []
    def handler(request):
        body = json.loads(request.content)
        requests.append(body)
        assert request.headers["Authorization"] == "Bearer secret"
        assert body["model"] == "text-embedding-v4"
        assert body["parameters"] == {"dimension": 64, "text_type": "query", "output_type": "dense"}
        rows = [{"text_index": i, "embedding": [float(text)] * 64} for i, text in enumerate(body["input"]["texts"])]
        return httpx.Response(200, json={"output": {"embeddings": list(reversed(rows))}})
    embedder = DashScopeEmbedder("secret", "https://example.com/embed", dimensions=64,
                                client=httpx.Client(transport=httpx.MockTransport(handler)))
    values = embedder.encode([str(i) for i in range(23)], text_type="query")
    assert [len(r["input"]["texts"]) for r in requests] == [10, 10, 3]
    assert values[:, 0].tolist() == list(range(23))


def test_dashscope_rerank_native_shape_and_input_order():
    def handler(request):
        body = json.loads(request.content)
        assert body == {"model": "qwen3-rerank", "input": {"query": "收入", "documents": ["a", "b"]},
                        "parameters": {"top_n": 2, "return_documents": False}}
        return httpx.Response(200, json={"output": {"results": [{"index": 1, "relevance_score": .9},
                                                                 {"index": 0, "relevance_score": .1}]}})
    rerank = DashScopeReranker("secret", "https://example.com/rerank", client=httpx.Client(transport=httpx.MockTransport(handler)))
    assert rerank.score("收入", ["a", "b"]) == [.1, .9]


@pytest.mark.parametrize("rows", [[], [{"index": 0, "relevance_score": .5}] * 2,
                                [{"index": True, "relevance_score": .1}, {"index": 0, "relevance_score": .2}],
                                [{"index": 0, "relevance_score": "nan"}, {"index": 1, "relevance_score": .2}]])
def test_reject_bad_rerank_indices_and_scores(rows):
    client = httpx.Client(transport=httpx.MockTransport(lambda req: httpx.Response(200, json={"output": {"results": rows}})))
    with pytest.raises(RetrievalAPIError):
        DashScopeReranker("secret", "https://example.com/rerank", client=client).score("q", ["a", "b"])


@pytest.mark.parametrize("payload", [
    {"output": {"embeddings": [{"text_index": 0, "embedding": [1.0]}]}},
    {"output": {"embeddings": [{"text_index": 2, "embedding": [1.0] * 64}]}},
    {"code": "SECRET ECHO", "message": "SECRET ECHO"},
])
def test_bad_embeddings_fail_without_response_echo(payload):
    client = httpx.Client(transport=httpx.MockTransport(lambda req: httpx.Response(200, json=payload)))
    with pytest.raises(RetrievalAPIError) as error:
        DashScopeEmbedder("secret", "https://example.com/embed", dimensions=64, client=client).encode(["a"])
    assert "SECRET" not in str(error.value)


def test_http_error_redacts_credentials():
    client = httpx.Client(transport=httpx.MockTransport(lambda req: httpx.Response(401, text="SECRET")))
    with pytest.raises(RetrievalAPIError, match="retrieval_http_401") as error:
        DashScopeEmbedder("secret", "https://example.com/embed", client=client).encode(["a"])
    assert "SECRET" not in str(error.value)


def test_cancellation_prevents_later_embedding_batches():
    calls = []
    embedder = None
    def handler(request):
        calls.append(request)
        embedder.cancelled = True
        return httpx.Response(200, json={"output": {"embeddings": [{"text_index": i, "embedding": [1.] * 64} for i in range(10)]}})
    embedder = DashScopeEmbedder("secret", "https://example.com/embed", dimensions=64,
                                client=httpx.Client(transport=httpx.MockTransport(handler)))
    with pytest.raises(RetrievalAPIError, match="cancelled"):
        embedder.encode(["a"] * 11)
    assert len(calls) == 1


def test_clean_chunk_persist_deduplicate_and_company_scope(tmp_path):
    text = clean_text("<html><nav>nav</nav><main>客户按年订阅。<script>secret</script> 合同可续签。</main></html>", html=True)
    assert "secret" not in text and "nav" not in text
    source = make_source("甲公司", "https://example.com/a", "收入", text * 100, kind="web")
    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    count = kb.add(source)
    assert count > 1 and kb.add(source) == 0
    for chunk in split_source(source):
        assert source.text[chunk.start:chunk.end] == chunk.text
    reopened = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    hits = reopened.retrieve("甲公司", "订阅合同")
    assert hits and hits[0].source.content_hash == source.content_hash
    assert reopened.retrieve("乙公司", "订阅合同") == []


def test_reranker_changes_dense_candidate_order(tmp_path):
    class Flat:
        name = "flat"
        def encode(self, texts, **kwargs):
            return np.array([[1., 0.]] * len(texts))
    class Reverse:
        name = "reverse"
        def score(self, query, documents):
            return [10. if text == "relevant" else 0. for text in documents]
    kb = KnowledgeBase(tmp_path / "kb.db", Flat(), Reverse())
    for text in ["irrelevant", "relevant"]:
        kb.add(make_source("ACME", f"https://example.com/{text}", text, text, kind="web"))
    assert kb.retrieve("ACME", "query", candidates=2, top_k=1)[0].chunk.text == "relevant"


def test_index_rejects_model_and_dimension_changes(tmp_path):
    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    other = DemoEmbedder()
    other.name = "other-model"
    with pytest.raises(ValueError, match="模型不一致"):
        KnowledgeBase(tmp_path / "kb.db", other, DemoReranker())


def test_local_material_stays_secondhand(tmp_path):
    p = tmp_path / "research.md"
    p.write_text("已有研究：收入规模仍待核实。")
    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    kb.ingest_file("企业", p)
    hit = kb.retrieve("企业", "收入规模")[0]
    assert hit.source.kind == "research_material" and hit.source.url == p.as_uri()


def test_literal_terms_add_an_exact_table_row_dense_retrieval_can_miss(tmp_path):
    kb = KnowledgeBase(tmp_path / "literal.db", DemoEmbedder(), DemoReranker())
    filler = " ".join(f"general market commentary paragraph {i}" for i in range(300))
    table = ("Date Open High Low Close Volume " +
             "Sep 21, 2026 371.64 378.36 371.07 375.30 36599600 " +
             "Sep 18, 2026 369.00 370.90 360.75 364.27 51922300 " + filler)
    kb.add(make_source("Tesla", "https://example.invalid/history", "历史价格", table, kind="web"))

    hits = kb.retrieve_many(["Tesla"], "股价是多少", candidates=10, top_k=8,
                            literal_terms=["Sep 21, 2026"])

    assert any("Sep 21, 2026 371.64 378.36 371.07 375.30" in hit.chunk.text for hit in hits)
