#!/usr/bin/env python3
"""Compute structural evaluation metrics from BusinessAgent V2 run artifacts.

This script deliberately measures only what the traces/state can prove:
citation structure, exact-quote acceptance, claim/gap status, retrieval yield,
token usage and wall-clock. It does NOT decide whether a claim is semantically
true; that requires the human/LLM judge protocol in evaluation_framework.md.

Usage:
    python3 score_runs.py
    python3 score_runs.py --runs-root ../../runs --out scorecard.json
    python3 score_runs.py --only-complete
"""
from __future__ import annotations

import argparse
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_RUNS = HERE.parent.parent / "runs"

OFFICIAL_AUTHORITIES = {"vendor_official", "regulator_filing"}
NUMBER_RE = re.compile(r"\d[\d,\.]*%?")


def as_time(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", "", text or "")


def number_signature(text: str) -> tuple[str, ...]:
    return tuple(sorted(NUMBER_RE.findall(text or "")))


def safe_div(num: float, den: float) -> float | None:
    return round(num / den, 4) if den else None


def pct(value: float | None) -> str:
    return "-" if value is None else f"{value * 100:.1f}%"


def collect(directory: Path) -> dict | None:
    state_path = directory / "state.json"
    trace_path = directory / "trace.jsonl"
    if not state_path.exists() or not trace_path.exists():
        return None
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    result = {}
    result_path = directory / "result.json"
    if result_path.exists():
        try:
            result = json.loads(result_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass

    questions = {q["id"]: q for q in state.get("questions", [])}
    claims = state.get("claims", [])
    evidence = state.get("evidence", [])
    gaps = state.get("gaps", [])
    sources = state.get("sources", [])
    source_by_id = {s["id"]: s for s in sources}

    # ---- trace counters -------------------------------------------------
    counters = Counter()
    node_seconds: dict[str, list[float]] = defaultdict(list)
    node_started: dict[str, datetime] = {}
    seen_claims: set[tuple[str, str]] = set()
    flagged_fact_ids: set[str] = set()
    numeric_fact_ids: set[str] = set()
    new_supported_by_round: Counter = Counter()
    supported_by_round: Counter = Counter()
    seen_claim_text: set[str] = set()
    first_seen_urls: set[str] = set()
    urls_by_round: dict[int, set[str]] = defaultdict(set)
    run_start = run_end = None

    for line in trace_path.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get("event")
        if kind == "run_start":
            run_start = as_time(event.get("time"))
        elif kind == "run_end":
            run_end = as_time(event.get("time"))
        elif kind == "model_end":
            usage = event.get("usage") or {}
            counters["model_calls"] += 1
            counters["input_tokens"] += usage.get("input_tokens", 0) or 0
            counters["output_tokens"] += usage.get("output_tokens", 0) or 0
        elif kind == "retrieval_api":
            resource = event.get("resource") or "unknown"
            counters[f"retrieval_{resource}_calls"] += 1
            counters[f"retrieval_{resource}_tokens"] += event.get("total_tokens", 0) or 0
            if event.get("error"):
                counters["retrieval_errors"] += 1
        elif kind == "search_end":
            counters["searches"] += 1
            counters["tavily_credits"] += (event.get("cost_metadata") or {}).get("credits") or 0
            if event.get("error"):
                counters["search_errors"] += 1
        elif kind == "page_end":
            counters["pages"] += 1
            if event.get("error"):
                counters["page_errors"] += 1
        elif kind == "evidence_extracted":
            counters["quotes_accepted"] += event.get("exact_quotes") or 0
            counters["quotes_rejected"] += event.get("rejected_quotes") or 0
        elif kind == "coverage":
            counters["coverage_assessments"] += 1
            if event.get("sufficient"):
                counters["coverage_sufficient"] += 1
        elif kind == "assessment":
            counters["assessments"] += 1
            if event.get("resolved"):
                counters["assessment_resolved"] += 1
        elif kind == "claim_number_not_in_citation":
            key = (str(event.get("claim_id")), str(event.get("numbers")))
            if key not in seen_claims:
                seen_claims.add(key)
                counters["numeric_flags"] += 1
            flagged_fact_ids.add(str(event.get("claim_id")))
        elif kind == "quote_rejected":
            counters["quote_reject_events"] += 1
        elif kind == "answer_rejected":
            counters["answer_rejected"] += 1
        elif kind == "node_start":
            node_started[event.get("node")] = as_time(event.get("time"))
        elif kind == "node_end":
            node = event.get("node")
            started = node_started.pop(node, None)
            ended = as_time(event.get("time"))
            if started and ended:
                node_seconds[node].append((ended - started).total_seconds())

    # ---- source / evidence structure -----------------------------------
    for source in sources:
        acquisition = source.get("acquisition") or {}
        question = questions.get(acquisition.get("question_id"))
        round_no = question["round"] if question else -1
        urls_by_round[round_no].add(source.get("url", ""))
    for round_no in sorted(urls_by_round):
        for url in urls_by_round[round_no]:
            first_seen_urls.add((round_no, url))

    official_evidence = 0
    for item in evidence:
        source = source_by_id.get(item.get("source_id"))
        if source and source.get("authority") in OFFICIAL_AUTHORITIES:
            official_evidence += 1
    duplicate_quotes = len(evidence) - len({e.get("quote", "").strip() for e in evidence})

    # ---- claim structure -----------------------------------------------
    fact_claims = [c for c in claims if c.get("kind") == "fact"]
    numeric_facts = [c for c in fact_claims if any(ch.isdigit() for ch in c.get("text", ""))]
    numeric_fact_ids = {c["id"] for c in numeric_facts}
    flagged_facts = flagged_fact_ids & numeric_fact_ids
    supported = sum(c.get("status") == "supported" for c in claims)
    unverified = sum(c.get("status") == "unverified" for c in claims)
    mixed = sum(c.get("status") == "mixed" for c in claims)
    cited = sum(bool(c.get("citations")) for c in claims)
    fact_supported = sum(c.get("status") == "supported" for c in fact_claims)

    answer_ids = state.get("answer_claim_ids", [])
    claim_by_id = {c["id"]: c for c in claims}
    answer_supported = sum(claim_by_id.get(i, {}).get("status") == "supported" for i in answer_ids)

    for claim in sorted(claims, key=lambda c: (questions.get(c.get("question_id"), {}).get("round", -1), c.get("id", ""))):
        if claim.get("status") != "supported":
            continue
        round_no = questions.get(claim.get("question_id"), {}).get("round", -1)
        supported_by_round[round_no] += 1
        normalized = normalize_text(claim.get("text", ""))
        if normalized not in seen_claim_text:
            seen_claim_text.add(normalized)
            new_supported_by_round[round_no] += 1

    # ---- gaps -----------------------------------------------------------
    open_gaps = [g for g in gaps if g.get("status") == "open"]
    resolved_gaps = [g for g in gaps if g.get("status") == "resolved"]
    high_priority_open = [g for g in open_gaps if (g.get("priority") or 3) >= 4]
    attempted_gap_ids = {q.get("parent_gap_id") for q in state.get("questions", []) if q.get("parent_gap_id")}
    attempted_gaps = [g for g in gaps if g.get("id") in attempted_gap_ids]

    followup_rounds = sorted({q.get("round") for q in state.get("questions", []) if (q.get("round") or 0) >= 2})
    followup_new_claims = sum(new_supported_by_round[r] for r in followup_rounds)
    followup_claims = sum(supported_by_round[r] for r in followup_rounds)
    followup_rounds_with_new = sum(1 for r in followup_rounds if new_supported_by_round[r] > 0)
    followup_rounds_with_supported = sum(1 for r in followup_rounds if supported_by_round[r] > 0)
    followup_rounds_with_new_url = sum(
        1 for r in followup_rounds if any(url for url in urls_by_round.get(r, set()))
    )

    # ---- limits / utilization -----------------------------------------
    limits = (result.get("metrics") or {}).get("limits") or {}
    used = {
        "rounds": state.get("rounds") or 0,
        "searches": counters["searches"],
        "pages": counters["pages"],
        "model_calls": counters["model_calls"],
        "embedding_calls": counters.get("retrieval_embedding_calls", 0),
        "reranker_calls": counters.get("retrieval_reranker_calls", 0),
    }
    utilization = {
        name: safe_div(value, limits.get(name))
        for name, value in used.items()
        if limits.get(name)
    }

    elapsed = (run_end - run_start).total_seconds() if run_start and run_end else None
    input_tokens = counters["input_tokens"]
    output_tokens = counters["output_tokens"]
    retrieval_tokens = sum(
        value for key, value in counters.items() if key.startswith("retrieval_") and key.endswith("_tokens")
    )

    metrics = {
        "run_id": state.get("run_id"),
        "batch": directory.parent.name,
        "directory": str(directory),
        "company": state.get("company"),
        "mode": state.get("mode"),
        "stop_reason": state.get("stop_reason"),
        "rounds": state.get("rounds"),
        "has_answer": bool(state.get("answer")),
        "answer_claims": len(answer_ids),
        "answer_claims_supported": answer_supported,
        "answer_claim_support_rate": safe_div(answer_supported, len(answer_ids)),
        "run_complete": bool(run_end and state.get("answer")),
        # fact reliability (structural, not semantic truth)
        "claims": len(claims),
        "fact_claims": len(fact_claims),
        "supported_claims": supported,
        "mixed_claims": mixed,
        "unverified_claims": unverified,
        "supported_claim_rate": safe_div(supported, len(claims)),
        "unverified_claim_rate": safe_div(unverified, len(claims)),
        "citation_coverage": safe_div(cited, len(claims)),
        "fact_support_rate_structural": safe_div(fact_supported, len(fact_claims)),
        "numeric_fact_claims": len(numeric_facts),
        "numeric_fact_claims_flagged": len(flagged_facts),
        "numeric_citation_flag_rate": safe_div(len(flagged_facts), len(numeric_facts)),
        "quotes_accepted": counters["quotes_accepted"],
        "quotes_rejected": counters["quotes_rejected"],
        "quote_acceptance_rate": safe_div(
            counters["quotes_accepted"], counters["quotes_accepted"] + counters["quotes_rejected"]
        ),
        "answer_rejected": counters["answer_rejected"],
        "evidence": len(evidence),
        "duplicate_quotes": duplicate_quotes,
        "official_evidence": official_evidence,
        "official_evidence_ratio": safe_div(official_evidence, len(evidence)),
        "sources": len(sources),
        "source_authority": dict(Counter(s.get("authority", "unknown") for s in sources)),
        # research completeness
        "gaps": len(gaps),
        "open_gaps": len(open_gaps),
        "resolved_gaps": len(resolved_gaps),
        "high_priority_open_gaps": len(high_priority_open),
        "gap_resolution_rate": safe_div(len(resolved_gaps), len(gaps)),
        "attempted_gaps": len(attempted_gaps),
        "attempted_gap_resolution_rate": safe_div(
            sum(g.get("status") == "resolved" for g in attempted_gaps), len(attempted_gaps)
        ),
        "coverage_assessments": counters["coverage_assessments"],
        "coverage_sufficient": counters["coverage_sufficient"],
        "coverage_sufficiency_rate": safe_div(
            counters["coverage_sufficient"], counters["coverage_assessments"]
        ),
        # multi-round effectiveness
        "followup_rounds": len(followup_rounds),
        "followup_questions": sum(1 for q in state.get("questions", []) if (q.get("round") or 0) >= 2),
        "followup_supported_claims": followup_claims,
        "followup_new_supported_claims": followup_new_claims,
        "followup_rounds_with_new_claim": followup_rounds_with_new,
        "followup_rounds_with_supported_claim": followup_rounds_with_supported,
        "followup_rounds_with_new_url": followup_rounds_with_new_url,
        "wasted_followup_rounds": len(followup_rounds) - followup_rounds_with_supported,
        "wasted_followup_rate": safe_div(
            len(followup_rounds) - followup_rounds_with_supported, len(followup_rounds)
        ),
        "new_text_claim_round_rate": safe_div(followup_rounds_with_new, len(followup_rounds)),
        "supported_claims_per_followup_round": safe_div(followup_claims, len(followup_rounds)),
        "new_text_claims_per_followup_round": safe_div(followup_new_claims, len(followup_rounds)),
        # A gap closing is the only unambiguous "decisive evidence" signal the
        # current state records. New URLs/quotes are too permissive to count.
        "decisive_evidence_rate": safe_div(len(resolved_gaps), len(followup_rounds)),
        # efficiency
        "elapsed_seconds": round(elapsed, 1) if elapsed is not None else None,
        "model_calls": counters["model_calls"],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "retrieval_tokens": retrieval_tokens,
        "total_tokens": input_tokens + output_tokens + retrieval_tokens,
        "searches": counters["searches"],
        "search_errors": counters["search_errors"],
        "search_success_rate": safe_div(counters["searches"] - counters["search_errors"], counters["searches"]),
        "pages": counters["pages"],
        "page_errors": counters["page_errors"],
        "page_success_rate": safe_div(counters["pages"] - counters["page_errors"], counters["pages"]),
        "embedding_calls": counters.get("retrieval_embedding_calls", 0),
        "reranker_calls": counters.get("retrieval_reranker_calls", 0),
        "tavily_credits": counters["tavily_credits"],
        "budget_utilization": utilization,
        "max_budget_utilization": max(utilization.values()) if utilization else None,
        "tokens_per_supported_claim": safe_div(input_tokens + output_tokens, supported),
        "seconds_per_supported_claim": (
            round(elapsed / supported, 2) if elapsed is not None and supported else None
        ),
        "new_claims_per_1k_tokens": (
            round(followup_new_claims / ((input_tokens + output_tokens) / 1000), 2)
            if input_tokens + output_tokens else None
        ),
        "node_seconds": {name: round(sum(values), 1) for name, values in node_seconds.items()},
    }
    return metrics


def aggregate(rows: list[dict]) -> dict:
    complete = [r for r in rows if r["run_complete"]]

    def summarize(sample: list[dict]) -> dict:
        def values(key):
            return [r[key] for r in sample if r.get(key) is not None]

        def stat(key, fn=statistics.mean):
            data = values(key)
            return round(fn(data), 4) if data else None

        def p90(key):
            data = sorted(values(key))
            if not data:
                return None
            index = max(0, math.ceil(0.9 * len(data)) - 1)
            return round(data[index], 4)

        return {
            "runs": len(sample),
            "stop_reasons": dict(Counter(r["stop_reason"] for r in sample)),
            "mean_supported_claim_rate": stat("supported_claim_rate"),
            "mean_fact_support_rate_structural": stat("fact_support_rate_structural"),
            "mean_numeric_citation_flag_rate": stat("numeric_citation_flag_rate"),
            "mean_quote_acceptance_rate": stat("quote_acceptance_rate"),
            "mean_official_evidence_ratio": stat("official_evidence_ratio"),
            "mean_coverage_sufficiency_rate": stat("coverage_sufficiency_rate"),
            "mean_gap_resolution_rate": stat("gap_resolution_rate"),
            "mean_attempted_gap_resolution_rate": stat("attempted_gap_resolution_rate"),
            "mean_high_priority_open_gaps": stat("high_priority_open_gaps"),
            "mean_wasted_followup_rate": stat("wasted_followup_rate"),
            "mean_decisive_evidence_rate": stat("decisive_evidence_rate"),
            "mean_new_text_claim_round_rate": stat("new_text_claim_round_rate"),
            "mean_supported_claims_per_followup_round": stat("supported_claims_per_followup_round"),
            "mean_new_text_claims_per_followup_round": stat("new_text_claims_per_followup_round"),
            "mean_elapsed_seconds": stat("elapsed_seconds"),
            "median_elapsed_seconds": stat("elapsed_seconds", statistics.median),
            "p90_elapsed_seconds": p90("elapsed_seconds"),
            "mean_input_tokens": stat("input_tokens"),
            "mean_output_tokens": stat("output_tokens"),
            "mean_total_tokens": stat("total_tokens"),
            "mean_searches": stat("searches"),
            "mean_pages": stat("pages"),
            "mean_page_success_rate": stat("page_success_rate"),
            "mean_max_budget_utilization": stat("max_budget_utilization"),
            "mean_tokens_per_supported_claim": stat("tokens_per_supported_claim"),
            "mean_seconds_per_supported_claim": stat("seconds_per_supported_claim"),
        }

    return {
        "runs_total": len(rows),
        "runs_complete": len(complete),
        "runs_with_answer": sum(r["has_answer"] for r in rows),
        "run_success_rate": safe_div(len(complete), len(rows)),
        "all_runs": summarize(rows),
        "complete_runs": summarize(complete),
    }


def markdown(rows: list[dict], summary: dict) -> str:
    lines = [
        "# BusinessAgent V2 结构指标得分卡",
        "",
        "> 本表只含可自动核验的结构指标；事实语义正确性、关键证据覆盖率需按 "
        "`evaluation_framework.md` 的人工/LLM 判定协议补齐。",
        "",
        "## 汇总",
        "",
        "| 指标 | 全部运行 | 完整运行 |",
        "|---|---|---|",
    ]
    labels = {
        "mean_supported_claim_rate": "结论支持率（自标注）",
        "mean_fact_support_rate_structural": "事实支持率（结构层）",
        "mean_numeric_citation_flag_rate": "数字未见于引用率",
        "mean_quote_acceptance_rate": "逐字引文接受率",
        "mean_official_evidence_ratio": "官方/监管证据占比",
        "mean_coverage_sufficiency_rate": "覆盖判定充分率",
        "mean_gap_resolution_rate": "缺口关闭率",
        "mean_attempted_gap_resolution_rate": "已尝试缺口关闭率",
        "mean_high_priority_open_gaps": "高优先级开放缺口/运行",
        "mean_wasted_followup_rate": "无支持结论的后续轮次率",
        "mean_decisive_evidence_rate": "决定性证据率（缺口关闭/后续轮）",
        "mean_new_text_claim_round_rate": "有新文本结论的后续轮次率（易饱和）",
        "mean_supported_claims_per_followup_round": "每后续轮支持结论",
        "mean_new_text_claims_per_followup_round": "每后续轮新文本结论（代理）",
        "mean_elapsed_seconds": "平均耗时（秒）",
        "median_elapsed_seconds": "耗时中位数（秒）",
        "p90_elapsed_seconds": "耗时 P90（秒）",
        "mean_total_tokens": "平均 Token",
        "mean_searches": "平均检索次数",
        "mean_pages": "平均网页读取数",
        "mean_page_success_rate": "网页读取成功率",
        "mean_max_budget_utilization": "最高预算利用率",
        "mean_tokens_per_supported_claim": "每支持结论 Token",
        "mean_seconds_per_supported_claim": "每支持结论秒数",
    }
    lines += [
        f"| 运行数 | {summary['runs_total']} | {summary['runs_complete']} |",
        f"| 产生 answer 的运行数 | {summary['runs_with_answer']} | {summary['runs_complete']} |",
        f"| 运行成功率 | {pct(summary['run_success_rate'])} | - |",
    ]
    for key, label in labels.items():
        all_value = summary["all_runs"].get(key)
        complete_value = summary["complete_runs"].get(key)
        def render(value):
            if value is None:
                return "-"
            if "rate" in key or "ratio" in key or "utilization" in key:
                return pct(value)
            return f"{value:.1f}" if isinstance(value, float) else str(value)
        lines.append(f"| {label} | {render(all_value)} | {render(complete_value)} |")
    lines += ["", "完整运行 = 有 `answer` 且写入 `run_end` 的运行。质量类指标请以“完整运行”列为准；"
              "运行成功率、成本与失败模式看“全部运行”。"]
    lines += ["", "## 逐运行", "",
              "| 运行 | 停止原因 | 轮次 | 耗时s | Token | 事实支持率 | 数字引用告警率 | 缺口关闭 | 无效后续轮 | 网页成功率 |",
              "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for row in sorted(rows, key=lambda r: (r["batch"], r["directory"])):
        lines.append(
            f"| {row['run_id']} | {row['stop_reason'] or '-'} | {row['rounds']} | "
            f"{row['elapsed_seconds'] if row['elapsed_seconds'] is not None else '-'} | "
            f"{row['total_tokens']} | {pct(row['fact_support_rate_structural'])} | "
            f"{pct(row['numeric_citation_flag_rate'])} | "
            f"{row['resolved_gaps']}/{row['gaps']} | {pct(row['wasted_followup_rate'])} | "
            f"{pct(row['page_success_rate'])} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS)
    parser.add_argument("--out", type=Path, default=HERE / "scorecard.json")
    parser.add_argument("--markdown", type=Path, default=HERE / "scorecard.md")
    parser.add_argument("--only-complete", action="store_true",
                        help="只输出有 answer 且写入 run_end 的运行")
    args = parser.parse_args()

    rows = []
    for state_path in sorted(args.runs_root.glob("**/state.json")):
        row = collect(state_path.parent)
        if row is None:
            continue
        if args.only_complete and not row["run_complete"]:
            continue
        rows.append(row)

    summary = aggregate(rows)
    payload = {"summary": summary, "runs": rows}
    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    args.markdown.write_text(markdown(rows, summary), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"\nwrote {args.out}\nwrote {args.markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
