import numpy as np


class SecurityEnvironment:
    STATES = ["normal", "scanning", "breach", "contained"]
    ACTIONS = ["monitor", "block_ip", "isolate_host", "report_incident"]

    def __init__(self):
        self.state_idx = 0
        self.steps = 0

    def reset(self) -> int:
        self.state_idx = 0
        self.steps = 0
        return self.state_idx

    def step(self, action_idx: int) -> tuple[int, float, bool]:
        self.steps += 1
        done = self.steps >= 20

        action = self.ACTIONS[action_idx]
        state = self.STATES[self.state_idx]

        if state == "normal" and action == "monitor":
            reward = 1.0
            self.state_idx = 0 if np.random.random() > 0.2 else 1
        elif state == "scanning" and action == "block_ip":
            reward = 2.0
            self.state_idx = 0 if np.random.random() > 0.1 else 2
        elif state == "breach" and action == "isolate_host":
            reward = 5.0
            self.state_idx = 3
        elif state == "breach" and action == "report_incident":
            reward = 3.0
            self.state_idx = 3
        elif state == "contained" and action == "report_incident":
            reward = 2.0
            self.state_idx = 0 if np.random.random() > 0.1 else 3
        else:
            reward = -1.0
            if state == "breach":
                self.state_idx = 2

        return self.state_idx, reward, done
