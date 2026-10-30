#!/usr/bin/env python3
"""Turn each run directory into a compact review file and aggregate usage.

The output is for human evaluation against the reference notes; it is not
ingested by the agent.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
MANIFEST = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
OUT = HERE / "review"


def latest_run(qid: str) -> Path | None:
    root = Path(MANIFEST["output_root"]) / qid
    runs = sorted(root.glob("*/result.json")) if root.exists() else []
    return runs[-1].parent if runs else None


def usage(directory: Path) -> dict:
    total = defaultdict(int)
    schemas = defaultdict(lambda: {"calls": 0, "input_tokens": 0, "output_tokens": 0})
    audit = Counter()
    searches = 0
    credits = 0
    for line in (directory / "trace.jsonl").read_text(encoding="utf-8").splitlines():
        event = json.loads(line)
        kind = event["event"]
        if kind == "model_end":
            use = event.get("usage") or {}
            schemas[event["schema"]]["calls"] += 1
            schemas[event["schema"]]["input_tokens"] += use.get("input_tokens", 0) or 0
            schemas[event["schema"]]["output_tokens"] += use.get("output_tokens", 0) or 0
            total["model_input_tokens"] += use.get("input_tokens", 0) or 0
            total["model_output_tokens"] += use.get("output_tokens", 0) or 0
        elif kind == "retrieval_api":
            total[f"{event.get('resource')}_tokens"] += event.get("total_tokens", 0) or 0
        elif kind == "search_end":
            searches += 1
            credits += (event.get("cost_metadata") or {}).get("credits") or 0
        elif kind in {"claim_number_not_in_citation", "claim_normalized", "quote_rejected",
                      "source_rejected", "gap_merged"}:
            audit[kind] += 1
    total["searches"] = searches
    total["tavily_credits"] = credits
    return {"totals": dict(total), "by_schema": dict(schemas), "audit": dict(audit)}


def main() -> int:
    OUT.mkdir(exist_ok=True)
    usage_rows = []
    for item in MANIFEST["questions"]:
        qid = item["id"]
        directory = latest_run(qid)
        if directory is None:
            print(f"{qid}: not run")
            continue
        state = json.loads((directory / "state.json").read_text(encoding="utf-8"))
        result = json.loads((directory / "result.json").read_text(encoding="utf-8"))
        use = usage(directory)
        lines = [f"# {qid} 运行摘要", "",
                 f"- 企业：{item['company']}", f"- 难度：{item['difficulty']}",
                 f"- 运行目录：`{directory}`", f"- 停止原因：{result.get('stop_reason')}",
                 f"- 轮次：{result.get('rounds')}；证据：{result.get('evidence')}；结论：{result.get('claims')}；开放缺口：{result.get('open_gaps')}",
                 f"- 用量：{json.dumps(result.get('metrics'), ensure_ascii=False)}", ""]
        if state.get("answer"):
            lines += ["## 结论摘要", "", state["answer"], "",
                      "引用结论：" + ", ".join(state.get("answer_claim_ids", [])), ""]
        lines += ["## 已支持结论", ""]
        for claim in state.get("claims", []):
            if claim["status"] in {"supported", "mixed", "contradicted"}:
                cites = ", ".join(f"{c['evidence_id']}({c['relation']})" for c in claim["citations"])
                lines += [f"- **{claim['id']}** [{claim['kind']}/{claim['status']}] {claim['text']}",
                          f"  - 引用：{cites}", f"  - 依据：{claim['rationale']}"]
        lines += ["", "## 待验证假设", ""]
        for claim in state.get("claims", []):
            if claim["kind"] == "hypothesis":
                lines += [f"- **{claim['id']}** {claim['text']}"]
        lines += ["", "## 证据缺口", ""]
        for gap in state.get("gaps", []):
            lines += [f"- {gap['id']} [{gap['status']}] {gap['description']}"]
        lines += ["", "## 来源", ""]
        for source in state.get("sources", []):
            lines += [f"- `{source.get('authority', 'unknown')}` {source['url']} — {source['title']}"]
        lines += ["", "## 调用量", "", "```json",
                  json.dumps(use, ensure_ascii=False, indent=2), "```", ""]
        (OUT / f"{qid}.md").write_text("\n".join(lines), encoding="utf-8")
        usage_rows.append({"id": qid, "directory": str(directory),
                           "result": result, "usage": use})
    (HERE / "usage.json").write_text(json.dumps(usage_rows, ensure_ascii=False, indent=2),
                                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
