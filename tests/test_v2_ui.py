import time

import pytest


def test_ui_load_blank_submission_and_offline_flow(tmp_path, monkeypatch):
    pytest.importorskip("streamlit")
    from streamlit.testing.v1 import AppTest
    from enterprise_agent import ui
    manager = ui.Jobs()
    monkeypatch.setattr(ui, "ROOT", tmp_path)
    monkeypatch.setattr(ui, "jobs", lambda: manager)
    try:
        app = AppTest.from_string("from enterprise_agent.ui import main\nmain()").run()
        assert not app.exception
        assert [t.label for t in app.tabs] == ["开始研究", "研究资料库", "研究记录"]
        assert manager.future is None  # Rendering never spends API calls.
        app.button[0].click().run()
        assert any("请填写" in error.value for error in app.error)
        assert manager.future is None
        next(b for b in app.button if b.label == "运行离线合成演示").click().run()
        assert manager.future is not None
        manager.future.result(timeout=10)
        app.run()
        assert not app.exception
        assert manager.directory is not None
        assert (manager.directory / "report.md").exists()
    finally:
        manager.cancel()
        manager.pool.shutdown(wait=True)
