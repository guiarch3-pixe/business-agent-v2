from __future__ import annotations

import json
import threading
from pathlib import Path

from enterprise_agent.schema import ResearchState, now


class Artifacts:
    def __init__(self, directory: Path):
        self.directory = directory
        self._lock = threading.Lock()
        self._sequence = 0

    def event(self, kind: str, **data):
        with self._lock:
            self._sequence += 1
            event = {"sequence": self._sequence, "time": now().isoformat(), "event": kind, **data}
            with (self.directory / "trace.jsonl").open("a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False) + "\n")

    def write(self, name: str, text: str):
        path = self.directory / name
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(text, encoding="utf-8")
        temporary.replace(path)

    def checkpoint(self, state: ResearchState):
        state = ResearchState.model_validate(state.model_dump())
        self.write("state.json", state.model_dump_json(indent=2))

    def finish(self, state: ResearchState, metrics: dict):
        self.checkpoint(state)
        self.write("report.md", render_report(state))
        self.write("result.json", json.dumps({"run_id": state.run_id, "mode": state.mode,
                    "stop_reason": state.stop_reason, "rounds": state.rounds,
                    "evidence": len(state.evidence), "claims": len(state.claims),
                    "open_gaps": sum(g.status == "open" and g.blocking for g in state.gaps),
                    "residual_gaps": sum(g.status == "open" and not g.blocking for g in state.gaps),
                    "resolved_gaps": sum(g.status == "resolved" for g in state.gaps),
                    "rounds_detail": round_details(state),
                    "metrics": metrics}, ensure_ascii=False, indent=2))


def round_details(state: ResearchState) -> list[dict]:
    """Per-round marginal value: what each additional round actually produced.

    Counts are derived from the persisted state, not from model prose, so a
    round that searched but produced no usable evidence is visibly empty.
    """
    questions = {q.id: q for q in state.questions}
    claims_by_round: dict[int, list] = {}
    evidence_by_round: dict[int, list] = {}
    for claim in state.claims:
        round_no = questions[claim.question_id].round if claim.question_id in questions else None
        claims_by_round.setdefault(round_no, []).append(claim)
    for item in state.evidence:
        round_no = questions[item.question_id].round if item.question_id in questions else None
        evidence_by_round.setdefault(round_no, []).append(item)
    details = []
    for question in sorted(state.questions, key=lambda q: q.round):
        if question.round == 0:
            continue
        round_no = question.round
        searches = [s for s in state.searches if s.question_id == question.id]
        new_claims = claims_by_round.get(round_no, [])
        new_evidence = evidence_by_round.get(round_no, [])
        new_sources = [s for s in state.sources
                       if s.acquisition and s.acquisition.question_id == question.id]
        new_gaps = [g for g in state.gaps if g.question_id == question.id]
        claim_ids = {c.id for c in new_claims}
        resolved = [g for g in state.gaps if g.status == "resolved"
                    and set(g.resolution_claim_ids) & claim_ids]
        target = next((g for g in state.gaps if g.id == question.parent_gap_id), None)
        if target is None:
            gap_status = "—"
        elif target in resolved:
            gap_status = "本轮关闭"
        elif target.status == "resolved":
            gap_status = "已关闭"
        elif target.blocking:
            gap_status = "开放/阻塞"
        else:
            gap_status = "开放/残留"
        errors = [s.error for s in searches if s.error]
        if resolved:
            value = "关闭缺口"
        elif new_evidence or new_claims:
            value = "有新增"
        elif errors:
            value = "搜索失败，无新增"
        else:
            value = "无新增有效证据"
        details.append({
            "round": round_no,
            "gap_id": target.id if target else None,
            "gap_description": target.description if target else "",
            "gap_status_after": gap_status,
            "question": question.text,
            "query": "；".join(s.query for s in searches),
            "search_errors": errors,
            "new_sources": len(new_sources),
            "new_evidence": len(new_evidence),
            "new_claims": len(new_claims),
            "new_claim_texts": [c.text for c in new_claims[:3]],
            "new_gaps": [g.description for g in new_gaps],
            "resolved_gaps": [g.description for g in resolved],
            "value": value,
        })
    return details


def render_report(state: ResearchState) -> str:
    labels = {"fact": "事实（来源陈述）", "deduction": "推导", "business_judgment": "商业判断", "hypothesis": "待验证假设"}
    resolved_count = sum(g.status == "resolved" for g in state.gaps)
    blocking_count = sum(g.status == "open" and g.blocking for g in state.gaps)
    residual_count = sum(g.status == "open" and not g.blocking for g in state.gaps)
    lines = [f"# {state.company}｜企业研究", "", f"研究问题：{state.goal}", "",
             f"模式：{state.mode}；停止原因：{state.stop_reason}；研究轮次：{state.rounds}", "",
             f"缺口：已关闭 {resolved_count}；阻塞待解决 {blocking_count}；残留未知 {residual_count}", "",
             "引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。", ""]
    if state.mode == "demo":
        lines += ["**离线合成演示：内容及来源均为测试夹具，不是真实企业研究。**", ""]
    if state.answer:
        claim_refs = "、".join(state.answer_claim_ids)
        lines += ["## 结论摘要", "", state.answer, "",
                  f"依据结论：{claim_refs}（详细证据见下方对应条目）", ""]
    details = round_details(state)
    if details:
        lines += ["## 每轮研究价值", "",
                  "新增数按代码持久化的证据、结论和来源统计；不把模型自述当作进展。", "",
                  "| 轮次 | 目标缺口 | 缺口状态 | 研究问题 | 搜索 | 新增来源 | 新增证据 | 新增结论 | 新开/关闭 | 判断 |",
                  "|---:|---|---|---|---|---:|---:|---:|---|---|"]
        for item in details:
            question = " ".join(item["question"].split())
            query = "；".join(item["query"].split("；")[:1])
            gap_label = f"{item['gap_id'] or '—'} {item['gap_description']}" if item.get("gap_id") else "—"
            if len(question) > 52:
                question = question[:51] + "…"
            if len(query) > 36:
                query = query[:35] + "…"
            if len(gap_label) > 48:
                gap_label = gap_label[:47] + "…"
            gap_text = "；".join(item["new_gaps"])[:60]
            lines.append(
                f"| {item['round']} | {gap_label} | {item.get('gap_status_after', '—')} | "
                f"{question} | {query or '—'} | {item['new_sources']} | "
                f"{item['new_evidence']} | {item['new_claims']} | "
                f"{len(item['new_gaps'])}/{len(item['resolved_gaps'])}"
                f"{('：' + gap_text) if gap_text else ''} | {item['value']} |")
        lines.append("")
    for kind, label in labels.items():
        lines += [f"## {label}", ""]
        for c in (x for x in state.claims if x.kind == kind):
            refs = " ".join(f"[{r.evidence_id}](#{r.evidence_id})（{r.relation}）" for r in c.citations)
            lines += [f"- **{c.id}** [{c.status}] {c.text} {refs}", f"  依据/推导：{c.rationale}"]
        lines.append("")
    lines += ["## 证据缺口", ""]
    for g in state.gaps:
        marker = "blocking" if g.blocking else "residual"
        lines += [f"- {g.id} [{g.status}/{marker}] {g.description}"]
        if g.status == "resolved":
            lines += [f"  模型评估关闭：{g.resolution_reason}；依据结论：{', '.join(g.resolution_claim_ids)}"]
    lines += ["", "## 问题与检索记录", ""]
    for q in state.questions:
        lines += [f"- {q.id} / 第 {q.round} 轮 / 缺口 {q.parent_gap_id or '初始问题'}：{q.text}"]
        for s in (x for x in state.searches if x.question_id == q.id):
            lines += [f"  Tavily {s.id}：{s.query}；结果 {len(s.urls)}；错误 {s.error or '无'}"]
    lines += ["", "## 原文摘录与追溯", ""]
    sources = {s.id: s for s in state.sources}
    for e in state.evidence:
        s = sources[e.source_id]
        # Generated anchor IDs contain only code-owned alphanumeric characters/underscores.
        lines += [f'<a id="{e.id}"></a>', f"### {e.id}", "", f"> {e.quote}", "",
                  f"来源：{s.title} — {s.url}", "",
                  f"类型：{s.kind}；读取时间：{s.retrieved_at.isoformat()}；截断：{s.truncated}", "",
                  f"问题 {e.question_id} → 分块 {e.chunk_id} → 来源 {s.id}；清洗后字符 [{e.start}, {e.end})", "",
                  f"SHA-256：`{s.content_hash}`；范围：{s.location}", ""]
        if s.acquisition:
            a = s.acquisition
            lines += [f"获取链：运行 {a.run_id} → 问题 {a.question_id} → 搜索 {a.search_id or '指定网页'} → {a.requested_url}",
                      f"检索词：{a.query or '无'}；当时的问题：{a.question}", ""]
    lines += ["完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。", ""]
    return "\n".join(lines)
