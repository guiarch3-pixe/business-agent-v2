"""A SIGTERM during a model call must still leave terminal artifacts.

The observed live interruption had a checkpoint but no result.json/report.md and
exit code 143: Python's default SIGTERM action bypasses ``finally``. This test
runs the real CLI cancellation helper in a child process and verifies the
graceful path end to end, without any network access.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

CHILD = r"""
import asyncio, json, sys
from pathlib import Path
from enterprise_agent.cli import _run_research_with_signals
from enterprise_agent.demo import (COMPANY, GOAL, NOTE, DemoEmbedder, DemoLLM, DemoReader,
                                   DemoReranker, DemoSearch)
from enterprise_agent.engine import ResearchEngine
from enterprise_agent.rag import KnowledgeBase, make_source
from enterprise_agent.settings import Limits

class SlowPlan(DemoLLM):
    async def generate(self, prompt, schema, **kwargs):
        if schema.__name__ == "Plan":
            await asyncio.sleep(60)
        return await super().generate(prompt, schema, **kwargs)

out = Path(sys.argv[1])
kb = KnowledgeBase(out / "kb.db", DemoEmbedder(), DemoReranker())
kb.add(make_source(COMPANY, "https://example.invalid/subscription", "合成材料", NOTE, kind="demo"))
engine = ResearchEngine(SlowPlan(), kb, DemoSearch(), DemoReader(), limits=Limits(rounds=3))
(result, sig) = asyncio.run(_run_research_with_signals(engine, COMPANY, GOAL, out / "runs", []))
state, directory = result
print(json.dumps({"directory": str(directory), "stop": state.stop_reason, "signal": sig}))
raise SystemExit(143 if sig == "SIGTERM" else 0)
"""


@pytest.mark.skipif(sys.platform == "win32", reason="POSIX signal semantics are the subject")
def test_sigterm_writes_cancelled_report_and_keeps_exit_code_143(tmp_path):
    out = tmp_path / "signal"
    out.mkdir()
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    process = subprocess.Popen([sys.executable, "-c", CHILD, str(out)], cwd=ROOT, env=env,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        trace = None
        deadline = time.monotonic() + 20
        while time.monotonic() < deadline:
            matches = list((out / "runs").glob("*/trace.jsonl"))
            if matches:
                trace = matches[0]
                if "model_start" in trace.read_text(encoding="utf-8"):
                    break
            if process.poll() is not None:
                break
            time.sleep(0.05)
        assert trace is not None, process.stderr.read() if process.poll() is not None else "no trace"
        process.send_signal(signal.SIGTERM)
        stdout, stderr = process.communicate(timeout=30)
    finally:
        if process.poll() is None:
            process.kill()

    assert process.returncode == 143, stderr
    result = json.loads(stdout.strip().splitlines()[-1])
    directory = Path(result["directory"])
    assert result["signal"] == "SIGTERM"
    assert (directory / "state.json").exists()
    assert (directory / "report.md").exists()
    saved = json.loads((directory / "result.json").read_text(encoding="utf-8"))
    assert saved["stop_reason"] == "cancelled"
    assert any(json.loads(line)["event"] == "signal_received"
               for line in (directory / "trace.jsonl").read_text(encoding="utf-8").splitlines())
