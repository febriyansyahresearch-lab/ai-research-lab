from typing import Any


class SimpleReflexAgent:
    def __init__(self, rules: dict[str, str]):
        self.rules = rules

    def act(self, percept: str) -> str:
        return self.rules.get(percept, "NO_OP")


class ModelBasedAgent:
    def __init__(self, rules: dict[str, str]):
        self.rules = rules
        self.state: dict[str, Any] = {}

    def update_state(self, percept: str):
        self.state["last_percept"] = percept
        self.state["step"] = self.state.get("step", 0) + 1

    def act(self, percept: str) -> str:
        self.update_state(percept)
        return self.rules.get(percept, "NO_OP")
