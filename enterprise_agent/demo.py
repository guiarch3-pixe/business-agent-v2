"""Explicitly synthetic, network-free acceptance scenario; never a live fallback."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import numpy as np

from enterprise_agent.engine import ResearchEngine
from enterprise_agent.rag import KnowledgeBase, make_source
from enterprise_agent.providers.base import ModelResponse, TokenUsage
from enterprise_agent.schema import Plan, Coverage, Extraction, Assessment, now
from enterprise_agent.tools.base import ToolResult, ToolRecord

COMPANY = "示例科技（合成）"
GOAL = "示例科技的收入模式及客户续费情况如何？"
NOTE = "合成示例材料：示例科技通过年度软件订阅收费。订阅合同按年签订。"
PAGE = "合成示例网页：示例科技在2025年的客户续费率为92%。该指标按续约客户数除以到期客户数计算。"


def terms(text):
    return set(re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text.casefold()))


class DemoEmbedder:
    name = "demo-hash-64-NOT-semantic"

    def encode(self, texts, *, text_type="document"):
        result = np.zeros((len(texts), 64), dtype=np.float32)
        for i, text in enumerate(texts):
            for token in terms(text):
                result[i, int(hashlib.sha256(token.encode()).hexdigest()[:8], 16) % 64] += 1
            result[i, 0] += .01
        return result


class DemoReranker:
    name = "demo-token-overlap-NOT-neural"

    def score(self, query, documents):
        return [float(len(terms(query) & terms(d))) for d in documents]


class DemoSearch:
    async def execute(self, query):
        return ToolResult(tool_name="synthetic_search", query_or_input=query,
                          records=[ToolRecord(content="Discovery-only synthetic snippet", source_url="https://example.invalid/retention",
                                              source_title="合成续费资料", retrieved_at=now())])


class DemoReader:
    async def execute(self, url):
        return ToolResult(tool_name="synthetic_reader", query_or_input=url,
                          records=[ToolRecord(content=PAGE, source_url=url, source_title="合成续费资料", retrieved_at=now())])


class DemoLLM:
    async def generate(self, prompt, schema, **kwargs):
        data = json.loads(prompt.split("DATA:\n", 1)[1])
        if schema is Plan:
            gap = next((g for g in data["open_gaps"] if g["id"] == "gap1"), data["open_gaps"][0])
            question = ("示例科技的收入模式是什么？" if not data["claims"] else
                        "示例科技2025年客户续费率是多少？" if gap["id"] == "gap1" else GOAL)
            output = Plan(gap_id=gap["id"], question=question, query=question, rationale="合成演示：逐轮处理未解决缺口")
        elif schema is Coverage:
            sufficient = "续费率" not in data["question"] or any("92%" in p["text"] for p in data["passages"])
            output = Coverage(sufficient=sufficient,
                              chunk_ids=[p["chunk_id"] for p in data["passages"]] if sufficient else [],
                              rationale="合成演示：检查所需字段", missing="客户续费率" if not sufficient else "")
        elif schema is Extraction:
            passages = data["passages"]
            target = next((p for p in passages if "92%" in p["text"]), passages[0]) if "续费率" in data["question"] else passages[0]
            selected = passages if data["question"] == GOAL else [target]
            output = Extraction(quotes=[{"chunk_id": p["chunk_id"], "quote": p["text"]} for p in selected])
        elif schema is Assessment:
            round_no = data["round"]
            ev = (next(e["id"] for e in data["evidence"] if "92%" in e["quote"])
                  if round_no == 2 else data["evidence"][0]["id"])
            claim = {"id": f"c{round_no}_1", "question_id": data["question_id"], "kind": "fact",
                     "text": "资料称企业按年收取订阅费。" if round_no == 1 else "合成资料披露2025年客户续费率为92%。",
                     "status": "supported", "citations": [{"evidence_id": ev, "relation": "supports"}],
                     "rationale": "仅依据合成演示原文。"}
            claims = [claim]
            if round_no == 1:
                for i, kind, text in [(2, "deduction", "合同按年到期，因此每年存在续约节点。"),
                                      (3, "business_judgment", "评估收入持续性需要补查客户续费数据。"),
                                      (4, "hypothesis", "客户可能持续续费，仍待验证。")]:
                    claims.append({**claim, "id": f"c1_{i}", "kind": kind, "text": text,
                                   "status": "unverified" if kind == "hypothesis" else "supported",
                                   "rationale": "合成示例推导，不代表真实企业判断。"})
            if round_no == 3:
                claims = [{**claim, "text": "企业按年收取订阅费，合成资料披露2025年客户续费率为92%。",
                           "citations": [{"evidence_id": e["id"], "relation": "supports"} for e in data["evidence"]]}]
            output = Assessment(claims=claims, resolve_gap=round_no != 1,
                                resolution_claim_ids=[claim["id"]] if round_no != 1 else [],
                                rationale="合成演示：先回答子问题，补齐续费证据后再综合回答原始问题。",
                                new_gaps=[{"description": "示例科技2025年客户续费率是多少？", "priority": 5, "claim_ids": ["c1_3"]}] if round_no == 1 else [])
        else:
            raise AssertionError(schema)
        return ModelResponse(output=output, model="synthetic-fixture-NOT-DeepSeek", usage=TokenUsage())


async def run_demo(output_dir: Path, *, on_event=None):
    # Separate DB prevents demo data/model identity contaminating real research.
    output_dir = Path(output_dir)
    kb = KnowledgeBase(output_dir / "demo-knowledge.sqlite3", DemoEmbedder(), DemoReranker())
    # A fresh company scope per demo permits rerunning the two-round scenario.
    import uuid
    company = COMPANY + "-" + uuid.uuid4().hex[:8]
    kb.add(make_source(company, "https://example.invalid/subscription", "合成年度订阅资料", NOTE, kind="demo"))
    engine = ResearchEngine(DemoLLM(), kb, DemoSearch(), DemoReader(), on_event=on_event)
    return await engine.run(company, GOAL, output_dir, mode="demo")
