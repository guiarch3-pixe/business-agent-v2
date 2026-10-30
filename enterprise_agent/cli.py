from __future__ import annotations

import argparse
import asyncio
import json
import os
import signal
import sys
from pathlib import Path

from enterprise_agent.settings import Limits, live_components, configured_kb, load_environment

ROOT = Path(__file__).resolve().parent.parent

#: Explicit research budgets for reproducible evaluation runs. These are not a
#: quality guarantee; they only set resource ceilings. Individual flags override
#: the selected preset.
PRESETS = {
    "easy": dict(rounds=6, searches=6, pages=12, model_calls=36, recovery_calls=4,
                 embedding_calls=300, reranker_calls=12, timeout=1200),
    "standard": dict(rounds=8, searches=8, pages=16, model_calls=48, recovery_calls=4,
                     embedding_calls=500, reranker_calls=16, timeout=1800),
    "deep": dict(rounds=10, searches=10, pages=20, model_calls=64, recovery_calls=4,
                 embedding_calls=700, reranker_calls=20, timeout=2400),
}


def parser():
    p = argparse.ArgumentParser(description="企业研究 Agent V2")
    sub = p.add_subparsers(dest="command", required=True)
    research = sub.add_parser("research", help="缺口驱动多轮研究")
    research.add_argument("--company", required=True)
    research.add_argument("--goal", required=True)
    research.add_argument("--company-alias", action="append", default=[],
                          help="比较题中的第二个企业名；用于识别其官方域名并复用其资料分区")
    research.add_argument("--source-url", action="append", default=[])
    research.add_argument("--db", type=Path, default=ROOT / "data/knowledge.sqlite3")
    research.add_argument("--output-dir", type=Path, default=ROOT / "runs")
    research.add_argument("--preset", choices=sorted(PRESETS), default=None,
                          help="预算预设；显式 --max-* 参数优先")
    defaults = Limits()
    research.add_argument("--max-rounds", type=int, default=None)
    research.add_argument("--max-searches", type=int, default=None)
    research.add_argument("--max-pages", type=int, default=None)
    research.add_argument("--max-model-calls", type=int, default=None)
    research.add_argument("--max-recovery-calls", type=int, default=None)
    research.add_argument("--max-embedding-calls", type=int, default=None)
    research.add_argument("--max-reranker-calls", type=int, default=None)
    research.add_argument("--top-k", type=int, default=defaults.top_k)
    research.add_argument("--candidates", type=int, default=defaults.candidates)
    research.add_argument("--no-progress-rounds", type=int, default=defaults.no_progress_rounds)
    research.add_argument("--gap-attempts", type=int, default=defaults.gap_attempts,
                          help="同一缺口连续占用轮次上限；超过后优先处理其他未尝试缺口")
    research.add_argument("--timeout", type=float, default=None)
    ingest = sub.add_parser("ingest", help="导入已有 UTF-8 txt/md/html 研究资料")
    ingest.add_argument("--company", required=True)
    ingest.add_argument("--db", type=Path, default=ROOT / "data/knowledge.sqlite3")
    ingest.add_argument("files", type=Path, nargs="+")
    demo = sub.add_parser("demo", help="不联网的合成演示")
    demo.add_argument("--output-dir", type=Path, default=ROOT / "runs/demo")
    sub.add_parser("doctor", help="只检查配置是否存在，不显示密钥、不调用 API")
    return p


async def _run_research_with_signals(engine, company, goal, output_dir, source_urls):
    """Cancel the research task on SIGTERM/SIGINT so terminal artifacts are written.

    Python's default SIGTERM action terminates the interpreter immediately, which
    bypasses ``finally`` and leaves a checkpoint without result.json/report.md.
    The signal is translated into task cancellation; the engine then records a
    ``cancelled`` stop reason and writes its terminal artifacts before re-raising.
    """
    task = asyncio.create_task(engine.run(company, goal, output_dir, source_urls=source_urls))
    received = []

    def request_stop(signame):
        received.append(signame)
        try:
            engine.event("signal_received", signal=signame)
        except Exception:
            pass
        task.cancel()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGTERM, signal.SIGINT):
        try:
            loop.add_signal_handler(sig, request_stop, sig.name)
        except (NotImplementedError, RuntimeError):
            pass
    try:
        return await task, received[0] if received else None
    except asyncio.CancelledError:
        return (engine.current, engine.directory), received[0] if received else None


def _budget(args, argument: str, key: str, default):
    value = getattr(args, argument)
    if value is not None:
        return value
    if args.preset:
        return PRESETS[args.preset][key]
    return default


def main(argv=None):
    args = parser().parse_args(argv)
    stop_signal = None
    try:
        if args.command == "doctor":
            load_environment()
            keys = ["DEEPSEEK_API_KEY", "TAVILY_API_KEY", "DASHSCOPE_API_KEY", "DASHSCOPE_WORKSPACE_ID"]
            for key in keys:
                print(f"{key}: {'已填写' if os.getenv(key, '').strip() else '未填写'}")
            print("配置检查不代表凭据或模型端点已通过联网验证。")
            return 0
        if args.command == "ingest":
            kb = configured_kb(args.db)
            for path in args.files:
                print(json.dumps({"file": str(path), "new_chunks": kb.ingest_file(args.company, path)}, ensure_ascii=False))
            return 0
        if args.command == "demo":
            from enterprise_agent.demo import run_demo
            state, directory = asyncio.run(run_demo(args.output_dir))
        else:
            from enterprise_agent.engine import ResearchEngine
            llm, kb, search, reader = live_components(args.db)
            limits = Limits(
                rounds=_budget(args, "max_rounds", "rounds", Limits.model_fields["rounds"].default),
                searches=_budget(args, "max_searches", "searches", Limits.model_fields["searches"].default),
                pages=_budget(args, "max_pages", "pages", Limits.model_fields["pages"].default),
                model_calls=_budget(args, "max_model_calls", "model_calls",
                                    Limits.model_fields["model_calls"].default),
                timeout=_budget(args, "timeout", "timeout", Limits.model_fields["timeout"].default),
                recovery_calls=_budget(args, "max_recovery_calls", "recovery_calls",
                                       Limits.model_fields["recovery_calls"].default),
                embedding_calls=_budget(args, "max_embedding_calls", "embedding_calls",
                                        Limits.model_fields["embedding_calls"].default),
                reranker_calls=_budget(args, "max_reranker_calls", "reranker_calls",
                                       Limits.model_fields["reranker_calls"].default),
                top_k=args.top_k, candidates=args.candidates,
                no_progress_rounds=args.no_progress_rounds, gap_attempts=args.gap_attempts)
            engine = ResearchEngine(llm, kb, search, reader, limits=limits,
                                    company_aliases=tuple(args.company_alias),
                                    on_event=lambda kind, data: print(f"[{kind}]", file=sys.stderr))
            (state, directory), stop_signal = asyncio.run(
                _run_research_with_signals(engine, args.company, args.goal,
                                           args.output_dir, args.source_url))
        print(json.dumps({"directory": str(directory), "stop_reason": state.stop_reason,
                          "rounds": state.rounds, "evidence": len(state.evidence), "claims": len(state.claims),
                          "signal": stop_signal}, ensure_ascii=False))
        if stop_signal == "SIGTERM":
            return 143
        if stop_signal == "SIGINT":
            return 130
        return 0 if state.claims and state.stop_reason in {
            "no_open_gaps", "no_blocking_gaps", "round_limit"} else 1
    except Exception as exc:
        # Configuration messages are controlled locally; provider exceptions never expose raw bodies.
        if type(exc) is ValueError:
            print(str(exc), file=sys.stderr)
        else:
            print(f"操作失败：{type(exc).__name__}（{getattr(exc, 'code', '检查配置或输入文件')}）", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
