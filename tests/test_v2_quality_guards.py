"""Offline guards for the quality failures observed in live runs.

These tests do not call any paid API. They cover the mechanisms that prevent:
* a formal-document gap from being closed with community or HTML evidence;
* one PDF gap being re-created under a new id every round;
* statements losing the product/heading context around a chunk;
* a two-product comparison drifting to one product.
"""
from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path

import pytest

from enterprise_agent.artifacts import Artifacts
from enterprise_agent.demo import (COMPANY, DemoEmbedder, DemoLLM, DemoReader, DemoReranker,
                                   DemoSearch, GOAL, NOTE)
from enterprise_agent.engine import (ResearchEngine, ResearchValidationError, StopResearch,
                                     focus_terms, gaps_are_duplicates)
from enterprise_agent.providers.base import ModelResponse, TokenUsage
from enterprise_agent.rag import KnowledgeBase, classify_authority, make_source, split_source
from enterprise_agent.schema import (Assessment, Citation, Claim, GapProposal, Evidence, Extraction,
                                     Gap, Hit, Plan, Question, QuoteProposal, ResearchState)
from enterprise_agent.settings import Limits


def engine_for(tmp_path, llm=None, limits=None):
    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    engine = ResearchEngine(llm or DemoLLM(), kb, None, None, limits=limits or Limits())
    engine.artifacts = Artifacts(tmp_path / "trace")
    engine.artifacts.directory.mkdir(parents=True, exist_ok=True)
    engine.deadline = time.monotonic() + 60
    return engine


def payload_of(prompt: str):
    return json.loads(prompt.split("DATA:\n", 1)[1])


def trace(directory):
    return [json.loads(line) for line in (directory / "trace.jsonl").read_text().splitlines()]


# --------------------------------------------------------------- source roles


@pytest.mark.parametrize(
    "url,kind,expected",
    [
        ("https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing", "web", "vendor_official"),
        ("https://www.microsoft.com/en-us/copilot/pricing/copilot-studio", "web", "vendor_official"),
        ("https://cdn-dynmedia-1.microsoft.com/is/content/guide.pdf", "web", "vendor_official"),
        ("https://learn.microsoft.com/en-us/answers/questions/2275889/reply", "web", "vendor_community"),
        ("https://answers.microsoft.com/en-us/topic/abc", "web", "vendor_community"),
        ("https://holgerimbery.blog/copilot-studio-licensing259", "web", "third_party"),
        ("file:///tmp/research.md", "research_material", "research_material"),
        ("https://example.invalid/synthetic", "demo", "demo"),
        ("https://www.sec.gov/Archives/edgar/data/1/filing.htm", "web", "regulator_filing"),
        ("https://data.sec.gov/api/xbrl/companyfacts/CIK0001318605.json", "web", "regulator_filing"),
    ],
)
def test_authority_distinguishes_hosting_domain_from_publisher(url, kind, expected):
    assert classify_authority(url, kind) == expected
    assert make_source("公司", url, "标题", "正文", kind=kind).authority == expected


def test_authority_recognizes_the_researched_company_domain_generically():
    assert classify_authority("https://www.stickermule.com/help/orders",
                              company="Sticker Mule") == "vendor_official"
    assert classify_authority("https://reviews.example.com/stickermule",
                              company="Sticker Mule") == "third_party"
    assert classify_authority("https://careers.stickermule.co.uk/jobs",
                              company="Sticker Mule") == "vendor_official"


def test_vector_retrieval_can_exclude_third_party_material_for_official_gaps(tmp_path):
    kb = KnowledgeBase(tmp_path / "authority.db", DemoEmbedder(), DemoReranker())
    official = make_source("Sticker Mule", "https://www.stickermule.com/help/orders",
                           "官方订单帮助", "客户可上传设计稿并确认数字样稿。", kind="web")
    third_party = make_source("Sticker Mule", "https://example.com/review",
                              "第三方评论", "客户可上传设计稿并确认数字样稿。", kind="web")
    kb.add(official)
    kb.add(third_party)
    legacy_authority = official.model_copy(update={"authority": "third_party"})
    with kb.connect() as db:
        db.execute("UPDATE sources SET payload=? WHERE id=?",
                   (legacy_authority.model_dump_json(), official.id))
        # The migration is intentionally one-shot; clear its marker to exercise it.
        db.execute("DELETE FROM metadata WHERE key='authority_scheme'")
    kb = KnowledgeBase(tmp_path / "authority.db", DemoEmbedder(), DemoReranker())

    hits = kb.retrieve("Sticker Mule", "订单设计样稿", authorities={"vendor_official"})

    assert hits
    assert {hit.source.authority for hit in hits} == {"vendor_official"}
    assert {hit.source.title for hit in hits} == {"官方订单帮助"}


def test_passages_carry_neighbouring_context_and_authority():
    text = "A" * 700 + " Copilot Studio 的购买前提是 Microsoft 365 计划。 " + "B" * 700
    source = make_source("Microsoft", "https://learn.microsoft.com/en-us/x", "Copilot Studio",
                         text, kind="web")
    chunk = next(c for c in split_source(source) if "Copilot Studio" in c.text)
    hit = Hit(chunk=chunk, source=source, vector_score=1.0, rerank_score=1.0)
    passage = ResearchEngine.passages([hit])[0]
    assert passage["source_authority"] == "vendor_official"
    assert passage["context_after"] or passage["context_before"]
    assert "text" in passage and "context_before" in passage and "context_after" in passage


# ------------------------------------------------------------- gap statistics


GAP_PDF_1 = ("仍需取得《Microsoft Copilot Studio 许可指南》PDF 正文中关于购买前提的逐字条款，"
             "以确认其是否明确写明“符合条件的 Microsoft 365 基础计划 + Copilot Studio 容量订阅”，"
             "以及是否单独提及 Power Platform 独立订阅/Premium 许可或特定容量计划；本轮仅有 Learn 网页与社区回帖摘录，未获得该 PDF 正文。")
GAP_PDF_2 = ("《Microsoft Copilot Studio 许可指南》PDF 正文仍未获取：需取得该 PDF 中关于 "
             "Copilot Studio 购买前提的逐字条款，确认是否写明“符合条件的 Microsoft 365 基础计划 + "
             "Copilot Studio 容量订阅”，以及是否单独提及 Power Platform 独立订阅、Premium 许可或特定容量计划。"
             "本轮证据仅来自定价页与 Learn 社区问答摘录，未包含该 PDF 正文。")
GAP_OTHER = ("需要确认 Microsoft 365 Copilot 的官方定价页是否以每位用户每月为单位标价，"
             "并核实未购买席位的用户仍可使用哪些基础功能。")


def test_rewritten_pdf_gap_is_detected_but_unrelated_gap_is_not():
    assert gaps_are_duplicates(GAP_PDF_1, GAP_PDF_2)
    assert not gaps_are_duplicates(GAP_PDF_1, GAP_OTHER)
    assert not gaps_are_duplicates("短缺口", "另一个短缺口")


def test_new_gap_is_merged_into_the_existing_one_and_trace_records_it(tmp_path):
    class RepeatsGap(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Assessment:
                data = payload_of(prompt)
                proposed = GAP_PDF_1 if data["round"] == 1 else GAP_PDF_2
                result.output.new_gaps = [*result.output.new_gaps,
                                          GapProposal(description=proposed, priority=5, claim_ids=[])]
            return result

    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成年度订阅资料",
                       NOTE, kind="demo"))
    engine = ResearchEngine(RepeatsGap(), kb, DemoSearch(), DemoReader(), limits=Limits(rounds=2))
    state, directory = asyncio.run(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))
    matching = [g for g in state.gaps if "Copilot Studio 许可指南" in g.description]
    assert len(matching) == 1
    assert any(event["event"] == "gap_merged" for event in trace(directory))


def test_one_paraphrased_quote_is_dropped_without_discarding_exact_quotes(tmp_path):
    class PartlyParaphrased(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Extraction:
                result.output.quotes.append(QuoteProposal(
                    chunk_id=result.output.quotes[0].chunk_id,
                    quote="You need a tenant prepaid pack before you can get this user license."))
            return result

    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成年度订阅资料",
                       NOTE, kind="demo"))
    engine = ResearchEngine(PartlyParaphrased(), kb, DemoSearch(), DemoReader(),
                            limits=Limits(rounds=1))
    state, directory = asyncio.run(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))
    assert state.stop_reason == "round_limit"
    assert state.evidence and state.claims
    assert engine.counts["recovery_calls"] == 0
    assert all("tenant prepaid pack" not in e.quote for e in state.evidence)
    events = trace(directory)
    assert any(e["event"] == "quote_rejected" for e in events)
    extracted = next(e for e in events if e["event"] == "evidence_extracted")
    assert extracted["rejected_quotes"] == 1 and extracted["exact_quotes"] >= 1


def test_assessment_may_cite_evidence_accepted_in_an_earlier_round(tmp_path):
    seen = {}

    class ReusesPriorEvidence(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Assessment:
                data = payload_of(prompt)
                if data["round"] == 2:
                    seen["prior"] = data["prior_evidence"]
                    result.output.claims[0].citations = [
                        Citation(evidence_id=data["prior_evidence"][0]["id"], relation="supports")]
                    result.output.claims[0].text = "此前已接受的合成材料显示企业按年订阅。"
                    result.output.resolve_gap = False
                    result.output.resolution_claim_ids = []
            return result

    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成年度订阅资料",
                       NOTE, kind="demo"))
    engine = ResearchEngine(ReusesPriorEvidence(), kb, DemoSearch(), DemoReader(), limits=Limits(rounds=2))
    state, _ = asyncio.run(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))
    assert state.stop_reason == "round_limit"
    assert seen["prior"] and seen["prior"][0]["source_authority"] == "demo"
    assert any("此前已接受" in c.text for c in state.claims)


def test_stable_topic_merges_reworded_gaps_even_when_prose_differs(tmp_path):
    class RepeatsTopic(DemoLLM):
        async def generate(self, prompt, schema, **kwargs):
            result = await super().generate(prompt, schema, **kwargs)
            if schema is Assessment:
                round_no = payload_of(prompt)["round"]
                description = ("需要官方 Copilot Studio 许可指南 PDF 第 4 页 How to Buy 一节的原文。"
                               if round_no == 1 else
                               "需要官方指南中关于定价路径与购买入口的完整条款。")
                result.output.new_gaps = [*result.output.new_gaps, GapProposal(
                    description=description, topic="copilot-studio-licensing-guide", priority=5)]
            return result

    kb = KnowledgeBase(tmp_path / "kb.db", DemoEmbedder(), DemoReranker())
    kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成年度订阅资料",
                       NOTE, kind="demo"))
    engine = ResearchEngine(RepeatsTopic(), kb, DemoSearch(), DemoReader(), limits=Limits(rounds=2))
    state, directory = asyncio.run(engine.run(COMPANY, GOAL, tmp_path / "runs", mode="demo"))
    matching = [g for g in state.gaps if g.topic == "copilot-studio-licensing-guide"]
    assert len(matching) == 1
    assert any(e["event"] == "gap_merged" and e.get("topic") == "copilot-studio-licensing-guide"
               for e in trace(directory))


# ------------------------------------- official/PDF resolution cannot be faked


def assessment_resolving(evidence_id="ev", claim_id="c1_1"):
    claim = Claim(id=claim_id, question_id="q1", kind="fact", text="官方指南写明购买前提。",
                  status="supported", rationale="测试夹具",
                  citations=[Citation(evidence_id=evidence_id, relation="supports")])
    return Assessment(claims=[claim], resolve_gap=True, resolution_claim_ids=[claim_id],
                      rationale="测试夹具关闭缺口", new_gaps=[])


class FixedAssessmentLLM:
    def __init__(self, assessment):
        self.assessment = assessment
        self.prompt = ""

    async def generate(self, prompt, schema, **kwargs):
        assert schema is Assessment
        self.prompt = prompt
        return ModelResponse(output=self.assessment, model="fixture", usage=TokenUsage())


def state_with_one_evidence(tmp_path, *, url, location, gap_text):
    source = make_source("Microsoft", url, "许可指南", "Copilot Studio 的购买前提是 Microsoft 365 计划。",
                         kind="web", location=location)
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev", question_id="q1", source_id=source.id, chunk_id=chunk.id,
                        quote=chunk.text, start=chunk.start, end=chunk.end)
    state = ResearchState(
        run_id="run-test", company="Microsoft", goal="比较两个产品的许可", rounds=1,
        questions=[Question(id="q0", text="比较两个产品的许可", round=0),
                   Question(id="q1", text="官方许可指南如何表述？", round=1, parent_gap_id="gap0")],
        gaps=[Gap(id="gap0", question_id="q0", description=gap_text, priority=5)],
        sources=[source], chunks=[chunk], evidence=[evidence])
    plan = Plan(gap_id="gap0", question="官方许可指南如何表述？", query="licensing guide",
                rationale="测试夹具")
    return state, plan, [Hit(chunk=chunk, source=source, vector_score=1, rerank_score=1)]


def run_assess(tmp_path, state, plan, hits):
    engine = engine_for(tmp_path, llm=FixedAssessmentLLM(assessment_resolving()))
    engine.current = state
    return asyncio.run(engine.assess({"research": state, "plan": plan, "hits": hits, "coverage": None}))


@pytest.mark.parametrize(
    "url,location",
    [
        # Vendor-hosted community reply: not a formal vendor document.
        ("https://learn.microsoft.com/en-us/answers/questions/1/reply", "cleaned page"),
        # Formal vendor page, but the gap explicitly requires PDF text.
        ("https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing", "cleaned page"),
    ],
)
def test_official_pdf_gap_cannot_close_on_community_or_html_evidence(tmp_path, url, location):
    state, plan, hits = state_with_one_evidence(
        tmp_path, url=url, location=location,
        gap_text="需要取得官方《许可指南》PDF 正文中关于购买前提的正式条款。")
    with pytest.raises(ResearchValidationError):
        run_assess(tmp_path, state, plan, hits)
    assert next(g for g in state.gaps if g.id == "gap0").status == "open"


def test_official_pdf_gap_closes_only_with_an_extracted_official_pdf(tmp_path):
    state, plan, hits = state_with_one_evidence(
        tmp_path,
        url="https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/guide.pdf",
        location="PDF pages 1-3 of 3; characters 0-100 of 100",
        gap_text="需要取得官方《许可指南》PDF 正文中关于购买前提的正式条款。")
    result = run_assess(tmp_path, state, plan, hits)
    gap = next(g for g in result["research"].gaps if g.id == "gap0")
    assert gap.status == "resolved"
    assert gap.resolution_claim_ids == ["c1_1"]


def test_numeric_audit_flags_numbers_absent_from_cited_quotes():
    class E:
        def __init__(self, quote):
            self.quote = quote
    claim = Claim(id="c1_1", question_id="q1", kind="fact", status="supported",
                  text="官方标价为 $30/用户/月，容量包 25,000 Credits，最高 20% 折扣。",
                  rationale="夹具", citations=[Citation(evidence_id="e1", relation="supports")])
    evidence = {"e1": E("Microsoft 365 Copilot $30 per user/month.")}
    assert ResearchEngine.unsupported_numbers(claim, evidence) == ["25,000", "20%"]
    good = Claim(id="c1_2", question_id="q1", kind="fact", status="supported",
                 text="官方标价为 $30/用户/月。", rationale="夹具",
                 citations=[Citation(evidence_id="e1", relation="supports")])
    assert ResearchEngine.unsupported_numbers(good, evidence) == []


def test_model_assessment_labels_are_repaired_against_their_citations():
    payload = {
        "rationale": "测试夹具",
        "claims": [
            {"id": "c1_1", "question_id": "q1", "kind": "fact", "status": "supported",
             "text": "无引用的事实", "rationale": "夹具", "citations": []},
            {"id": "c1_2", "question_id": "q1", "kind": "fact", "status": "supported",
             "text": "只有反证", "rationale": "夹具",
             "citations": [{"evidence_id": "e1", "relation": "contradicts"}]},
            {"id": "c1_3", "question_id": "q1", "kind": "deduction", "status": "supported",
             "text": "正反都有", "rationale": "夹具",
             "citations": [{"evidence_id": "e1", "relation": "supports"},
                           {"evidence_id": "e2", "relation": "contradicts"}]},
            {"id": "c1_4", "question_id": "q1", "kind": "hypothesis", "status": "supported",
             "text": "假设不能已支持", "rationale": "夹具",
             "citations": [{"evidence_id": "e1", "relation": "supports"}]},
            {"id": "c1_5", "question_id": "q1", "kind": "business_judgment", "status": "supported",
             "text": "无引用的判断", "rationale": "夹具", "citations": []},
        ],
    }
    normalized = Assessment.normalize_payload(payload)
    assessment = Assessment.model_validate(normalized)
    assert (assessment.claims[0].kind, assessment.claims[0].status) == ("hypothesis", "unverified")
    assert assessment.claims[1].status == "contradicted"
    assert assessment.claims[2].status == "mixed"
    assert assessment.claims[3].status == "unverified"
    assert assessment.claims[4].status == "unverified"


# ------------------------------------------- comparison balance and retry guard


def test_focus_terms_are_the_compared_products_not_generic_words():
    goal = ("Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？")
    assert focus_terms(goal) == ["Microsoft 365 Copilot", "Copilot Studio"]
    assert focus_terms("Microsoft 365 企业版包含哪些协作工具？") == ["Microsoft 365"]


class FixedPlanLLM:
    def __init__(self, plan):
        self.plan = plan
        self.prompt = ""

    async def generate(self, prompt, schema, **kwargs):
        assert schema is Plan
        self.prompt = prompt
        return ModelResponse(output=self.plan, model="fixture", usage=TokenUsage())


def comparison_state():
    source = make_source("Microsoft", "https://learn.microsoft.com/en-us/x", "Copilot Studio",
                         "Copilot Studio 按租户容量计费。", kind="web")
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev", question_id="q0", source_id=source.id, chunk_id=chunk.id,
                        quote=chunk.text, start=chunk.start, end=chunk.end)
    goal = ("Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？")
    return ResearchState(
        run_id="run-test", company="Microsoft", goal=goal,
        questions=[Question(id="q0", text=goal, round=0)],
        gaps=[Gap(id="gap0", question_id="q0", description=goal, priority=5),
              Gap(id="gap1", question_id="q0", description="Microsoft 365 Copilot 的每用户定价是多少？", priority=5),
              Gap(id="gap2", question_id="q0", description="Copilot Studio 的容量计费前提是什么？", priority=5)],
        sources=[source], chunks=[chunk], evidence=[evidence])


def test_comparison_guard_rejects_a_plan_that_only_chases_the_covered_product(tmp_path):
    state = comparison_state()
    plan = Plan(gap_id="gap2", question="Copilot Studio 的容量计费前提是什么？",
                query="Copilot Studio capacity", rationale="测试夹具")
    engine = engine_for(tmp_path, llm=FixedPlanLLM(plan))
    engine.current = state
    with pytest.raises(ResearchValidationError, match="unbalanced"):
        asyncio.run(engine.plan({"research": state, "plan": None, "hits": [], "coverage": None}))


def test_comparison_guard_also_catches_a_large_but_nonzero_skew(tmp_path):
    state = comparison_state()
    # Add a second Copilot Studio source/evidence so the under-covered side is no
    # longer at zero; the 2x skew guard must still fire.
    source = make_source("Microsoft", "https://learn.microsoft.com/en-us/y", "Copilot Studio",
                         "Copilot Studio 的容量包为每包 25,000 个 Copilot Credits。", kind="web")
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev2", question_id="q0", source_id=source.id, chunk_id=chunk.id,
                        quote=chunk.text, start=chunk.start, end=chunk.end)
    state = state.model_copy(update={"sources": [*state.sources, source],
                                     "chunks": [*state.chunks, chunk],
                                     "evidence": [*state.evidence, evidence]})
    for index in range(6):
        claim = Claim(id=f"cx{index}", question_id="q0", kind="fact", status="supported",
                      text="Microsoft 365 Copilot 按用户计费。", rationale="测试夹具",
                      citations=[Citation(evidence_id="ev", relation="supports")])
        state.claims.append(claim)
    plan = Plan(gap_id="gap1", question="Microsoft 365 Copilot 的每用户定价是多少？",
                query="M365 Copilot pricing", rationale="测试夹具")
    engine = engine_for(tmp_path, llm=FixedPlanLLM(plan))
    engine.current = state
    with pytest.raises(ResearchValidationError, match="unbalanced"):
        asyncio.run(engine.plan({"research": state, "plan": None, "hits": [], "coverage": None}))


def test_gap_attempt_cap_forces_an_untried_gap_before_revisiting(tmp_path):
    goal = "单一主题研究"
    state = ResearchState(
        run_id="run-test", company="企业", goal=goal,
        questions=[Question(id="q0", text=goal, round=0),
                   Question(id="q1", text="子问题一", round=1, parent_gap_id="gap0"),
                   Question(id="q2", text="子问题二", round=2, parent_gap_id="gap0")],
        gaps=[Gap(id="gap0", question_id="q0", description="已被反复追查的缺口", priority=5),
              Gap(id="gap1", question_id="q1", description="尚未尝试的缺口", priority=4)])
    plan = Plan(gap_id="gap0", question="再次追查", query="again", rationale="测试夹具")
    engine = engine_for(tmp_path, llm=FixedPlanLLM(plan), limits=Limits(gap_attempts=2))
    engine.current = state
    with pytest.raises(ResearchValidationError, match="revisiting"):
        asyncio.run(engine.plan({"research": state, "plan": None, "hits": [], "coverage": None}))


def test_business_workflow_goal_requires_process_mapping_before_agent_speculation(tmp_path):
    goal = "Sticker Mule 企业目前商业链路，哪些链路可以接入定制化 agent？"
    state = ResearchState(run_id="workflow-test", company="Sticker Mule", goal=goal,
                          questions=[Question(id="q0", text=goal, round=0)],
                          gaps=[Gap(id="gap0", question_id="q0", description=goal, priority=5)])
    plan = Plan(gap_id="gap0", question="订单的设计确认流程是什么？",
                query="Sticker Mule order design approval", rationale="先了解实际流程")
    llm = FixedPlanLLM(plan)
    engine = engine_for(tmp_path, llm=llm)
    engine.current = state

    asyncio.run(engine.plan({"research": state, "plan": None, "hits": [], "coverage": None}))

    prompt_data = payload_of(llm.prompt)
    instruction = prompt_data["task_specific_instruction"]
    assert "端到端步骤" in instruction
    assert "不要用 AI 招聘广告推断已有 agent" in instruction
    assert "不要围绕同一项“是否公开披露 AI”换词搜索" in instruction


def test_business_workflow_assessment_prioritizes_decision_relevant_claims(tmp_path):
    goal = "Sticker Mule 的商业链路中，哪些步骤适合接入定制化 agent？"
    source = make_source("Sticker Mule", "https://www.stickermule.com/help/orders",
                         "订单帮助", "客户上传设计稿后先检查数字样稿，再确认订单。", kind="web")
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev_workflow", question_id="q1", source_id=source.id,
                        chunk_id=chunk.id, quote=chunk.text, start=chunk.start, end=chunk.end)
    state = ResearchState(
        run_id="workflow-assess-test", company="Sticker Mule", goal=goal, rounds=1,
        questions=[Question(id="q0", text=goal, round=0),
                   Question(id="q1", text="设计确认流程有哪些步骤？", round=1, parent_gap_id="gap0")],
        gaps=[Gap(id="gap0", question_id="q0", description=goal)],
        sources=[source], chunks=[chunk], evidence=[evidence])
    claim = Claim(id="c1_1", question_id="q1", kind="fact", status="supported",
                  text="订单包含设计稿上传、数字样稿检查和客户确认步骤。",
                  rationale="摘录逐项说明了流程。", citations=[
                      Citation(evidence_id=evidence.id, relation="supports")])
    llm = FixedAssessmentLLM(Assessment(claims=[claim], rationale="保留流程缺口。"))
    engine = engine_for(tmp_path, llm=llm)
    engine.current = state
    engine.plan_state = None
    asyncio.run(engine.assess({
        "research": state,
        "plan": Plan(gap_id="gap0", question="设计确认流程有哪些步骤？",
                     query="Sticker Mule proof approval", rationale="流程问题"),
        "hits": [Hit(chunk=chunk, source=source, vector_score=1.0, rerank_score=1.0)],
        "coverage": None,
    }))

    instruction = payload_of(llm.prompt)["task_specific_instruction"]
    assert "具体流程步骤" in instruction
    assert "不要把“某来源是第三方”" in instruction
    assert "未核实的接入能力标记为假设" in instruction


def test_official_gap_retrieval_keeps_readable_third_party_context(tmp_path):
    kb = KnowledgeBase(tmp_path / "mixed.db", DemoEmbedder(), DemoReranker())
    kb.add(make_source("Microsoft", "https://www.microsoft.com/en-us/pricing",
                       "官方定价页（只有拦截页）", "Your request has been blocked. ",
                       kind="web"))
    kb.add(make_source("Microsoft", "https://example.com/review",
                       "第三方价格对比", "Microsoft 365 E3 年付标价为每位用户每月 39 美元。",
                       kind="web"))
    goal = "Microsoft 365 E3 的官方标价是多少？"
    state = ResearchState(run_id="mixed", company="Microsoft", goal=goal,
                          questions=[Question(id="q0", text=goal, round=0)],
                          gaps=[Gap(id="gap0", question_id="q0", description=goal, priority=5)])
    plan = Plan(gap_id="gap0", question=goal, query="Microsoft 365 E3 official price",
                rationale="测试夹具")
    engine = engine_for(tmp_path)
    engine.kb = kb

    result = asyncio.run(engine.retrieve({"research": state, "plan": plan,
                                          "hits": [], "coverage": None}))

    authorities = {hit.source.authority for hit in result["hits"]}
    assert "vendor_official" in authorities
    assert "third_party" in authorities


def test_invalid_summary_is_dropped_without_losing_validated_claims(tmp_path):
    goal = "Sticker Mule 的样稿流程是什么？"
    source = make_source("Sticker Mule", "https://www.stickermule.com/help/orders",
                         "订单帮助", "客户上传设计稿后先检查数字样稿，再确认订单。", kind="web")
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev_flow", question_id="q1", source_id=source.id,
                        chunk_id=chunk.id, quote=chunk.text, start=chunk.start, end=chunk.end)
    state = ResearchState(
        run_id="summary-test", company="Sticker Mule", goal=goal, rounds=1,
        questions=[Question(id="q0", text=goal, round=0),
                   Question(id="q1", text="样稿流程？", round=1, parent_gap_id="gap0")],
        gaps=[Gap(id="gap0", question_id="q0", description=goal)],
        sources=[source], chunks=[chunk], evidence=[evidence])
    claim = Claim(id="c1_1", question_id="q1", kind="fact", status="supported",
                  text="流程为上传设计稿、检查数字样稿、客户确认。", rationale="原文直接支持。",
                  citations=[Citation(evidence_id=evidence.id, relation="supports")])
    llm = FixedAssessmentLLM(Assessment(claims=[claim], rationale="回答流程。",
                                        answer="流程为上传、检查样稿、确认。",
                                        answer_claim_ids=["c_missing"]))
    engine = engine_for(tmp_path, llm=llm)
    engine.current = state

    result = asyncio.run(engine.assess({
        "research": state,
        "plan": Plan(gap_id="gap0", question="样稿流程？",
                     query="Sticker Mule proof", rationale="流程问题"),
        "hits": [Hit(chunk=chunk, source=source, vector_score=1.0, rerank_score=1.0)],
        "coverage": None,
    }))

    assert len(result["research"].claims) == 1
    assert result["research"].answer == ""


def test_report_renders_the_validated_answer_first():
    from enterprise_agent.artifacts import render_report
    state = ResearchState(run_id="render", company="企业", goal="价格是多少？",
                          answer="价格为 39 美元。",
                          questions=[Question(id="q0", text="价格是多少？", round=0)],
                          gaps=[Gap(id="gap0", question_id="q0", description="价格是多少？")])
    report = render_report(state)
    assert report.index("## 结论摘要") < report.index("## 事实")
    assert "价格为 39 美元。" in report


def test_round_details_show_marginal_value_from_persisted_state():
    from enterprise_agent.artifacts import round_details
    source = make_source("企业", "https://example.com/a", "来源", "收入为 100 万元。", kind="web")
    chunk = split_source(source)[0]
    evidence = Evidence(id="ev_r", question_id="q1", source_id=source.id, chunk_id=chunk.id,
                        quote=chunk.text, start=chunk.start, end=chunk.end)
    claim = Claim(id="c1_1", question_id="q1", kind="fact", status="supported",
                  text="收入为 100 万元。", rationale="原文。",
                  citations=[Citation(evidence_id="ev_r", relation="supports")])
    state = ResearchState(
        run_id="rounds", company="企业", goal="收入是多少？", rounds=2,
        questions=[Question(id="q0", text="收入是多少？", round=0),
                   Question(id="q1", text="查收入", round=1, parent_gap_id="gap0"),
                   Question(id="q2", text="查成本", round=2, parent_gap_id="gap0")],
        gaps=[Gap(id="gap0", question_id="q0", description="收入是多少？")],
        sources=[source], chunks=[chunk], evidence=[evidence], claims=[claim])
    details = round_details(state)
    assert details[0]["new_evidence"] == 1 and details[0]["new_claims"] == 1
    assert details[0]["value"] == "有新增"
    assert details[1]["new_evidence"] == 0 and details[1]["value"] == "无新增有效证据"


def test_residual_gap_does_not_force_another_round(tmp_path):
    goal = "价格是多少？"
    state = ResearchState(
        run_id="residual", company="企业", goal=goal,
        questions=[Question(id="q0", text=goal, round=0)],
        gaps=[Gap(id="gap0", question_id="q0", description="官方 PDF 原文尚未取得",
                  blocking=False)])
    engine = engine_for(tmp_path)
    engine.current = state
    with pytest.raises(StopResearch, match="no_blocking_gaps"):
        asyncio.run(engine.plan({"research": state, "plan": None, "hits": [], "coverage": None}))
