import json
import numpy as np

class QLearning:
    def __init__(self, filename="q_table.npy"):
        self.filename = filename
        self.q_table = self.load_q_table()

    def load_q_table(self):
        try:
            return np.load(self.filename, allow_pickle=True).item()
        except FileNotFoundError:
            return {}

    def save_q_table(self):
        np.save(self.filename, self.q_table)

    def update_q_value(self, state, action, reward, learning_rate=0.1, discount_factor=0.9):
        key = str(state)
        if key not in self.q_table:
            self.q_table[key] = {}
        if action not in self.q_table[key]:
            self.q_table[key][action] = 0

        self.q_table[key][action] += learning_rate * (
            reward + discount_factor * max(self.q_table[key].values(), default=0) - self.q_table[key][action]
        )
        self.save_q_table()

    def get_best_action(self, state):
        key = str(state)
        if key in self.q_table and self.q_table[key]:
            return max(self.q_table[key], key=self.q_table[key].get)
        return None
