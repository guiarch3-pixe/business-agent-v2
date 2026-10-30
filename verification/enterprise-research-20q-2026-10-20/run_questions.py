#!/usr/bin/env python3
"""Run the 20-question benchmark against the live V2 agent.

Only ``goal`` and company metadata are sent to the agent. The ``expected``
fields in ``manifest.json`` are evaluation notes and are never added to the
prompt, the knowledge database, or the command line.

Usage:
    WEB_READER_MIRROR=https://r.jina.ai python3 run_questions.py
    WEB_READER_MIRROR=https://r.jina.ai python3 run_questions.py --only Q1,Q4
    WEB_READER_MIRROR=https://r.jina.ai python3 run_questions.py --jobs 3
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import subprocess
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
PY = ROOT / ".venv/bin/python"
MANIFEST = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))
TIMEOUTS = {
    "easy": (1500, 1200),
    "standard": (2100, 1800),
    "deep": (2700, 2400),
}
_PRINT_LOCK = threading.Lock()


def parse_run(stdout: str) -> dict | None:
    for line in reversed(stdout.splitlines()):
        line = line.strip()
        if line.startswith("{") and '"directory"' in line:
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                return None
    return None


def run_one(item: dict, force: bool) -> dict:
    qid = item["id"]
    output_root = Path(MANIFEST["output_root"])
    qdir = output_root / qid
    existing = sorted(qdir.glob("*/result.json")) if qdir.exists() else []
    if existing and not force:
        with _PRINT_LOCK:
            print(f"[skip] {qid}: already has {existing[-1]}", flush=True)
        return {"id": qid, "directory": str(existing[-1].parent), "skipped": True}

    qdir.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(PY), "-m", "enterprise_agent.cli", "research",
        "--company", item["company"],
        "--goal", item["goal"],
        "--db", MANIFEST["db"],
        "--output-dir", str(qdir),
        "--preset", item["preset"],
        "--timeout", str(TIMEOUTS[item["preset"]][1]),
    ]
    for alias in item.get("company_aliases", []):
        cmd += ["--company-alias", alias]
    env = os.environ.copy()
    env.setdefault("WEB_READER_MIRROR", "https://r.jina.ai")
    started = time.time()
    with _PRINT_LOCK:
        print(f"[run] {qid} {item['company']} preset={item['preset']}", flush=True)
    try:
        proc = subprocess.run(cmd, cwd=ROOT, env=env, text=True, capture_output=True,
                              timeout=TIMEOUTS[item["preset"]][0])
        returncode, stdout, stderr = proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        returncode = -9
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = "harness timeout"
    elapsed = round(time.time() - started, 1)
    log = HERE / "logs" / f"{qid}.log"
    log.write_text(stdout + "\n--- STDERR ---\n" + stderr, encoding="utf-8")
    parsed = parse_run(stdout) or {}
    record = {
        "id": qid,
        "company": item["company"],
        "difficulty": item["difficulty"],
        "preset": item["preset"],
        "exit_code": returncode,
        "elapsed_seconds": elapsed,
        "directory": parsed.get("directory"),
        "stop_reason": parsed.get("stop_reason"),
        "rounds": parsed.get("rounds"),
        "evidence": parsed.get("evidence"),
        "claims": parsed.get("claims"),
        "log": str(log),
    }
    with _PRINT_LOCK:
        print(json.dumps(record, ensure_ascii=False), flush=True)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", default="", help="逗号分隔的题号，例如 Q1,Q2")
    parser.add_argument("--force", action="store_true", help="已有 result.json 也重跑")
    parser.add_argument("--jobs", type=int, default=1, help="并发题数")
    args = parser.parse_args()
    wanted = {x.strip().upper() for x in args.only.split(",") if x.strip()}
    items = [x for x in MANIFEST["questions"] if not wanted or x["id"] in wanted]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        records = list(pool.map(lambda item: run_one(item, args.force), items))
    (HERE / "runs.json").write_text(json.dumps(records, ensure_ascii=False, indent=2),
                                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
