import pytest
from auto_response.src.agent import ResponseAgent


def test_agent_act():
    agent = ResponseAgent(n_states=4, n_actions=4)
    action = agent.act(0, training=False)
    assert 0 <= action < 4


def test_agent_update():
    agent = ResponseAgent(n_states=4, n_actions=4, lr=0.1)
    agent.update(0, 1, 1.0, 2)
    assert agent.q_table[0, 1] != 0
