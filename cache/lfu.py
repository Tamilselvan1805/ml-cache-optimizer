from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.freq = defaultdict(int)

    def get(self, key):
        if key in self.cache:
            self.freq[key] += 1
            return True
        return False

    def put(self, key):
        if key in self.cache:
            self.freq[key] += 1
            return

        if len(self.cache) >= self.cap:
            lfu = min(self.freq, key=self.freq.get)
            del self.cache[lfu]
            del self.freq[lfu]

        self.cache[key] = True
        self.freq[key] = 1