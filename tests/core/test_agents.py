import pytest
from src.core.agents import SimpleReflexAgent, ModelBasedAgent


def test_simple_reflex_agent():
    rules = {"dirty": "clean", "clean": "no_op"}
    agent = SimpleReflexAgent(rules)
    assert agent.act("dirty") == "clean"
    assert agent.act("clean") == "no_op"


def test_model_based_agent():
    rules = {"dirty": "clean", "clean": "no_op"}
    agent = ModelBasedAgent(rules)
    assert agent.act("dirty") == "clean"
    assert agent.state["step"] == 1
