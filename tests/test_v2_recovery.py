import asyncio
import json

from enterprise_agent.demo import DemoLLM
from enterprise_agent.schema import Extraction, ResearchState
from enterprise_agent.settings import Limits
from test_v2_workflow import fixture_engine, execute, events


class OnceBadQuote(DemoLLM):
    def __init__(self):
        self.extract_calls = 0
        self.feedback_seen = False

    async def generate(self, prompt, schema, **kwargs):
        result = await super().generate(prompt, schema, **kwargs)
        if schema is Extraction:
            self.extract_calls += 1
            data = json.loads(prompt.split("DATA:\n", 1)[1])
            if self.extract_calls == 1:
                result.output.quotes[0].quote += "。这是补全的内容"
            else:
                self.feedback_seen = "validation_feedback" in data
        return result


def test_bad_quote_is_corrected_once_with_feedback_and_shared_budget(tmp_path):
    model = OnceBadQuote()
    engine = fixture_engine(tmp_path, llm=model, limits=Limits(rounds=1))
    state, directory = execute(engine, tmp_path)
    assert state.stop_reason == "round_limit"
    assert model.extract_calls == 2 and model.feedback_seen
    assert engine.counts["model_calls"] == 5 and engine.counts["recovery_calls"] == 1
    assert state.evidence and state.claims
    assert all("补全的内容" not in e.quote for e in state.evidence)
    assert any(x["event"] == "quote_rejected" for x in events(directory))
    ResearchState.model_validate_json((directory / "state.json").read_text())


def test_recovery_never_refreshes_model_budget(tmp_path):
    model = OnceBadQuote()
    engine = fixture_engine(tmp_path, llm=model, limits=Limits(model_calls=3, recovery_calls=2))
    state, _ = execute(engine, tmp_path)
    assert state.stop_reason == "error" and not state.evidence
    assert model.extract_calls == 1 and engine.counts["model_calls"] == 3
    assert engine.counts["recovery_calls"] == 0


def test_recovery_can_be_disabled(tmp_path):
    model = OnceBadQuote()
    state, _ = execute(fixture_engine(tmp_path, llm=model, limits=Limits(recovery_calls=0)), tmp_path)
    assert state.stop_reason == "error" and model.extract_calls == 1


def test_large_finite_vectors_do_not_normalize_to_zero():
    import numpy as np
    from enterprise_agent.rag import _vectors
    values = _vectors([[1e30, 1e30]], 1)
    assert np.linalg.norm(values[0]) > .99
