import random

class CacheEnv:
    def __init__(self, capacity, requests):
        self.capacity = capacity
        self.requests = requests

    def reset(self):
        self.cache = []
        self.index = 0
        self.history = {}
        return self._get_state()

    def _get_state(self):
        state = []

        for item in self.cache:
            freq = self.history.get(item, 0)
            recency = 1 if item in self.cache[-2:] else 0
            state.append((freq, recency))

        while len(state) < self.capacity:
            state.append((0, 0))

        return tuple(state)

    def step(self, action, use_hybrid=True):
        req = self.requests[self.index]
        self.index += 1

        self.history[req] = self.history.get(req, 0) + 1

        if req in self.cache:
            reward = 3
        else:
            if len(self.cache) < self.capacity:
                self.cache.append(req)
                reward = -1
            else:
                if use_hybrid and random.random() < 0.7:
                    action = min(
                        range(len(self.cache)),
                        key=lambda i: self.history.get(self.cache[i], 0)
                    )

                evicted = self.cache[action]
                evicted_freq = self.history.get(evicted, 0)

                reward = -1 - (0.1 * evicted_freq)
                self.cache[action] = req

        done = self.index >= len(self.requests)
        return self._get_state(), reward, done