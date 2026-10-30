"""Local Chinese workspace. Work is started only by an explicit button."""
from __future__ import annotations

import asyncio
import concurrent.futures
import json
import threading
import uuid
from pathlib import Path

import streamlit as st

from enterprise_agent.cli import ROOT
from enterprise_agent.engine import ResearchEngine
from enterprise_agent.schema import ResearchState
from enterprise_agent.settings import live_components, configured_kb, Limits


class Jobs:
    def __init__(self):
        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.lock = threading.Lock()
        self.future = None
        self.loop = None
        self.task = None
        self.cancel_requested = False
        self.events = []
        self.directory = None

    def event(self, kind, data):
        with self.lock:
            self.events.append({"event": kind, **data})

    def start(self, company, goal, rounds, demo=False, limits=None):
        with self.lock:
            if self.future and not self.future.done():
                return False
            self.events = []
            self.directory = None
            self.cancel_requested = False
            self.future = self.pool.submit(self.work, company, goal, rounds, demo, limits)
            return True

    def work(self, company, goal, rounds, demo, limits):
        async def run():
            with self.lock:
                self.loop, self.task = asyncio.get_running_loop(), asyncio.current_task()
                if self.cancel_requested:
                    self.task.cancel()
            if demo:
                from enterprise_agent.demo import run_demo
                return await run_demo(ROOT / "runs/demo", on_event=self.event)
            components = live_components(ROOT / "data/knowledge.sqlite3")
            engine = ResearchEngine(*components, limits=limits or Limits(rounds=rounds), on_event=self.event)
            return await engine.run(company, goal, ROOT / "runs")
        try:
            result = asyncio.run(run())
            self.directory = result[1]
            return result[1]
        except asyncio.CancelledError:
            return None
        finally:
            with self.lock:
                self.loop = self.task = None

    def cancel(self):
        with self.lock:
            self.cancel_requested = True
            if self.loop and self.task:
                self.loop.call_soon_threadsafe(self.task.cancel)


@st.cache_resource
def jobs():
    return Jobs()


def show_report(directory, key_prefix="history"):
    try:
        state = ResearchState.model_validate_json((directory / "state.json").read_text())
    except Exception:
        st.error("研究状态文件缺失或校验失败。")
        return
    st.subheader(state.company)
    st.caption(f"{state.mode} · {state.rounds} 轮 · {state.stop_reason or '进行中 / 中断'}")
    a, b, c = st.columns(3)
    a.metric("结论", len(state.claims))
    b.metric("原文证据", len(state.evidence))
    c.metric("未解决缺口", sum(g.status == "open" for g in state.gaps))
    report_path = directory / "report.md"
    if report_path.exists():
        report = report_path.read_text(encoding="utf-8")
        st.download_button("下载研究报告", report, file_name="report.md", key=key_prefix + str(directory))
        st.markdown(report, unsafe_allow_html=False)
    else:
        st.info("尚未生成终态报告；下方为已保存研究状态。")
    with st.expander("完整证据链 / 状态 JSON"):
        st.json(state.model_dump(mode="json"))


def main():
    st.set_page_config(page_title="企业研究 Agent V2", page_icon="🔎", layout="wide")
    st.title("企业研究 Agent")
    st.caption("提出问题 → 查证资料 → 形成结论 → 追查证据缺口")
    manager = jobs()
    research, materials, history = st.tabs(["开始研究", "研究资料库", "研究记录"])
    with research:
        with st.form("research"):
            company = st.text_input("企业名称")
            goal = st.text_area("你希望查清的问题", placeholder="例如：企业的收入模式是什么？哪些证据支持其竞争优势？")
            defaults = Limits()
            rounds = st.number_input("最多调查轮次", min_value=1, max_value=30, value=defaults.rounds)
            with st.expander("研究预算与检索范围"):
                st.caption("这些是资源上限，达到上限时保留未解决缺口；更多调用不代表结论更可靠。")
                searches = st.number_input("最多外部搜索次数", 0, 60, defaults.searches)
                pages = st.number_input("最多网页读取次数", 0, 300, defaults.pages)
                model_calls = st.number_input("最多 DeepSeek 调用次数", 1, 300, defaults.model_calls)
                recovery_calls = st.number_input("其中最多校正调用次数", 0, 30, defaults.recovery_calls)
                embedding_calls = st.number_input("最多 Embedding 调用次数", 1, 1000, defaults.embedding_calls)
                reranker_calls = st.number_input("最多 Reranker 调用次数", 1, 100, defaults.reranker_calls)
                minutes = st.number_input("总时限（分钟）", 1, 120, int(defaults.timeout / 60))
                candidates = st.number_input("向量召回候选数", 6, 100, defaults.candidates)
                top_k = st.number_input("重排后保留片段数", 1, 20, defaults.top_k)
                no_progress = st.number_input("连续无新增资料或研究进展后停止的轮数", 1, 10, defaults.no_progress_rounds)
                gap_attempts = st.number_input("同一缺口最多连续调查轮次", 1, 10, defaults.gap_attempts)
            submitted = st.form_submit_button("开始调查")
        if submitted:
            if not company.strip() or not goal.strip():
                st.error("请填写企业名称和研究问题。")
            elif top_k > candidates:
                st.error("保留片段数不能超过召回候选数。")
            else:
                limits = Limits(rounds=rounds, searches=searches, pages=pages, model_calls=model_calls,
                                recovery_calls=recovery_calls,
                                embedding_calls=embedding_calls, reranker_calls=reranker_calls,
                                timeout=minutes*60, candidates=candidates, top_k=top_k,
                                no_progress_rounds=no_progress, gap_attempts=gap_attempts)
                if not manager.start(company.strip(), goal.strip(), rounds, limits=limits):
                    st.info("已有调查正在运行，请等待或停止当前调查。")
        if st.button("运行离线合成演示"):
            if not manager.start("", "", 4, demo=True):
                st.info("已有调查正在运行。")

        @st.fragment(run_every=2)
        def progress():
            future = manager.future
            if future is None:
                return
            if not future.done():
                st.info("正在调查，已保存的结果可在研究记录中查看。")
                if st.button("停止当前调查"):
                    manager.cancel()
            else:
                try:
                    directory = future.result()
                    if directory:
                        show_report(directory, "active")
                    else:
                        st.info("调查已停止。已保存的记录可在研究记录中查看。")
                except Exception as exc:
                    st.error(str(exc) if type(exc) is ValueError else f"启动失败：{type(exc).__name__}，请检查本机配置。")
            with manager.lock:
                events = manager.events[-12:]
            with st.expander("调查进展"):
                for event in events:
                    st.text(json.dumps(event, ensure_ascii=False))
        progress()
    with materials:
        st.write("已有报告、访谈记录和网页文本可先导入。研究时先检索这些资料，证据不足再搜索外网。")
        material_company = st.text_input("资料所属企业", key="material_company")
        uploaded = st.file_uploader("选择 UTF-8 文本材料", type=["txt", "md", "html", "htm"], accept_multiple_files=True)
        if st.button("导入资料"):
            if not material_company.strip() or not uploaded:
                st.error("请填写企业名称并选择材料。")
            elif manager.future and not manager.future.done():
                st.info("请等待当前调查结束后再导入资料。")
            else:
                try:
                    kb = configured_kb(ROOT / "data/knowledge.sqlite3")
                    for upload in uploaded:
                        if upload.size > 2_000_000:
                            raise ValueError("单份材料上限 2 MB")
                        content = upload.getvalue()
                        content.decode("utf-8")
                        folder = ROOT / "data/materials" / uuid.uuid4().hex
                        folder.mkdir(parents=True)
                        path = folder / Path(upload.name).name
                        path.write_bytes(content)
                        try:
                            count = kb.ingest_file(material_company.strip(), path)
                        except Exception:
                            path.unlink()
                            folder.rmdir()
                            raise
                        st.success(f"{path.name}：导入 {count} 个分块")
                except Exception as exc:
                    st.error(str(exc) if type(exc) is ValueError else f"导入失败：{type(exc).__name__}")
    with history:
        if st.button("刷新研究记录"):
            st.rerun()
        paths = sorted((ROOT / "runs").glob("**/state.json"), key=lambda p: p.stat().st_mtime, reverse=True)
        if paths:
            selected = st.selectbox("选择研究记录", paths, format_func=lambda p: str(p.parent.relative_to(ROOT / "runs")))
            show_report(selected.parent)
        else:
            st.info("暂无研究记录。")


if __name__ == "__main__":
    main()
