import numpy as np
import random

class QAgent:
    def __init__(self, capacity, lr=0.1, gamma=0.9,
                 epsilon=1.0, epsilon_min=0.05, epsilon_decay=0.995):

        self.q = {}
        self.lr = lr
        self.gamma = gamma

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

        self.capacity = capacity

    def get_q(self, state):
        if state not in self.q:
            self.q[state] = np.zeros(self.capacity)
        return self.q[state]

    def act(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.capacity - 1)

        q_vals = self.get_q(state)
        max_q = np.max(q_vals)
        actions = [i for i, q in enumerate(q_vals) if q == max_q]
        return random.choice(actions)

    def update(self, state, action, reward, next_state):
        q_vals = self.get_q(state)
        next_q = np.max(self.get_q(next_state))

        td_target = reward + self.gamma * next_q
        q_vals[action] += self.lr * (td_target - q_vals[action])

    def decay_epsilon(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)