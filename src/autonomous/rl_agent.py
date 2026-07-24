import numpy as np


class QLearningAgent:
    def __init__(self, n_states: int, n_actions: int, lr: float = 0.1, gamma: float = 0.99, epsilon: float = 0.1):
        self.q_table = np.zeros((n_states, n_actions))
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.n_actions = n_actions

    def act(self, state: int) -> int:
        if np.random.random() < self.epsilon:
            return np.random.randint(self.n_actions)
        return int(np.argmax(self.q_table[state]))

    def update(self, state: int, action: int, reward: float, next_state: int):
        best_next = np.max(self.q_table[next_state])
        td_target = reward + self.gamma * best_next
        self.q_table[state, action] += self.lr * (td_target - self.q_table[state, action])
