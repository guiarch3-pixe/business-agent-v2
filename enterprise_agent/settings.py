from __future__ import annotations

import os
from pathlib import Path
from pydantic import Field, model_validator
from dotenv import load_dotenv
from enterprise_agent.schema import Model


class Limits(Model):
    rounds: int = Field(default=6, ge=1, le=30)
    searches: int = Field(default=8, ge=0, le=60)
    pages: int = Field(default=24, ge=0, le=300)
    model_calls: int = Field(default=36, ge=1, le=300)
    # A long multi-round run can hit more than two malformed proposals; two was too
    # few for a ten-round complex case. These calls still consume the model budget.
    recovery_calls: int = Field(default=4, ge=0, le=30)
    embedding_calls: int = Field(default=160, ge=1, le=1000)
    reranker_calls: int = Field(default=18, ge=1, le=100)
    timeout: float = Field(default=1200, gt=0, le=7200)
    candidates: int = Field(default=40, ge=6, le=100)
    top_k: int = Field(default=10, ge=1, le=20)
    no_progress_rounds: int = Field(default=2, ge=1, le=10)
    # After this many attempts on one gap, the planner must give other open gaps a
    # turn before revisiting it. This is a breadth guard, not a quality claim.
    gap_attempts: int = Field(default=2, ge=1, le=10)

    @model_validator(mode="after")
    def retrieval_sizes(self):
        if self.top_k > self.candidates:
            raise ValueError("top_k must not exceed candidates")
        return self


def load_environment():
    # Explicit V2 path, independent of the shell/Streamlit working directory.
    load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=False)


def live_components(db_path: Path):
    from enterprise_agent.providers.deepseek import DeepSeekLLM
    from enterprise_agent.tools.tavily import TavilySearchTool
    from enterprise_agent.tools.web_reader import WebPageReader
    from enterprise_agent.rag import KnowledgeBase, LocalEmbedder, LocalReranker
    load_environment()
    if not os.getenv("DEEPSEEK_API_KEY", "").strip():
        raise ValueError("请在 V2/.env 中填写 DEEPSEEK_API_KEY")
    kb = configured_kb(db_path)
    llm = DeepSeekLLM(os.environ["DEEPSEEK_API_KEY"], model=os.getenv("DEEPSEEK_MODEL", "deepseek-flash"),
                      base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"), max_output_tokens=6000)
    search = (TavilySearchTool(os.environ["TAVILY_API_KEY"], max_results=5,
                               search_depth=os.getenv("TAVILY_SEARCH_DEPTH", "basic"))
              if os.getenv("TAVILY_API_KEY", "").strip() else None)
    reader = WebPageReader(
        max_chars=int(os.getenv("WEB_READER_MAX_CHARS", "400000")),
        max_bytes=int(os.getenv("WEB_READER_MAX_BYTES", "8000000")),
        # Off unless explicitly configured: the mirror sends the requested URL to
        # a third-party text-rendering service. It is only used after the direct
        # read fails or returns an anti-bot interstitial.
        mirror_prefix=os.getenv("WEB_READER_MIRROR", "").strip() or None,
    )
    return llm, kb, search, reader


def local_kb(db_path: Path):
    from enterprise_agent.rag import KnowledgeBase, LocalEmbedder, LocalReranker
    load_environment()
    return KnowledgeBase(db_path,
                         LocalEmbedder(os.getenv("LOCAL_EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")),
                         LocalReranker(os.getenv("LOCAL_RERANKER_MODEL", "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1")))


def configured_kb(db_path: Path):
    from enterprise_agent.providers.dashscope import DashScopeEmbedder, DashScopeReranker
    from enterprise_agent.rag import KnowledgeBase
    load_environment()
    backend = os.getenv("RAG_BACKEND", "dashscope")
    if backend == "local":
        return local_kb(db_path)
    if backend != "dashscope":
        raise ValueError("RAG_BACKEND 仅支持 dashscope 或 local")
    workspace = os.getenv("DASHSCOPE_WORKSPACE_ID", "").strip()
    region = os.getenv("DASHSCOPE_REGION", "cn-beijing").strip()
    base = os.getenv("DASHSCOPE_BASE_URL", "").strip().rstrip("/")
    if not base:
        import re
        if not re.fullmatch(r"[a-zA-Z0-9-]+", workspace):
            raise ValueError("请填写 DASHSCOPE_WORKSPACE_ID，或设置控制台提供的 DASHSCOPE_BASE_URL（以 /api/v1 结尾）")
        if not re.fullmatch(r"[a-z0-9-]+", region):
            raise ValueError("DASHSCOPE_REGION 格式不正确")
        base = f"https://{workspace}.{region}.maas.aliyuncs.com/api/v1"
    key = os.getenv("DASHSCOPE_API_KEY", "")
    return KnowledgeBase(db_path,
        DashScopeEmbedder(key, base + "/services/embeddings/text-embedding/text-embedding",
                         os.getenv("EMBEDDING_MODEL", "text-embedding-v4"),
                         dimensions=int(os.getenv("EMBEDDING_DIMENSIONS", "1024"))),
        DashScopeReranker(key, base + "/services/rerank/text-rerank/text-rerank",
                         os.getenv("RERANKER_MODEL", "qwen3-rerank")))
