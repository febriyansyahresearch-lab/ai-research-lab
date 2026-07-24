import pytest
from src.autonomous.rl_agent import QLearningAgent


def test_q_agent_act():
    agent = QLearningAgent(n_states=5, n_actions=3)
    action = agent.act(0)
    assert 0 <= action < 3


def test_q_agent_update():
    agent = QLearningAgent(n_states=5, n_actions=3)
    agent.update(0, 1, 1.0, 2)
    assert agent.q_table[0, 1] != 0
