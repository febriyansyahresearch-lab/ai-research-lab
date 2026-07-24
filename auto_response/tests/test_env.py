import pytest
from auto_response.src.environment import SecurityEnvironment


def test_env_reset():
    env = SecurityEnvironment()
    state = env.reset()
    assert state == 0
    assert env.steps == 0


def test_env_step_returns_tuple():
    env = SecurityEnvironment()
    env.reset()
    result = env.step(0)
    assert len(result) == 3
    assert isinstance(result[0], int)
    assert isinstance(result[1], float)
    assert isinstance(result[2], bool)
