from cache.lru import LRUCache
from cache.lfu import LFUCache
from rl.environment import CacheEnv
from rl.agent import QAgent
from utils.parser import load_requests, normalize_requests
from utils.metrics import hit_ratio
import config


def run_lru(requests):
    cache = LRUCache(config.CACHE_SIZE)
    hits = 0
    for r in requests:
        if cache.get(r):
            hits += 1
        else:
            cache.put(r)
    return hits


def run_lfu(requests):
    cache = LFUCache(config.CACHE_SIZE)
    hits = 0
    for r in requests:
        if cache.get(r):
            hits += 1
        else:
            cache.put(r)
    return hits


def run_rl(requests):
    env = CacheEnv(config.CACHE_SIZE, requests)
    agent = QAgent(config.CACHE_SIZE)

    hits = 0

    for _ in range(config.EPISODES):
        state = env.reset()
        done = False

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)

            if reward > 0:
                hits += 1

            agent.update(state, action, reward, next_state)
            state = next_state

        agent.decay_epsilon()

    return hits // config.EPISODES


def main():
    raw = load_requests("data/apache_logs", config.MAX_REQUESTS)
    requests = normalize_requests(raw)

    lru_hits = run_lru(requests)
    lfu_hits = run_lfu(requests)
    rl_hits = run_rl(requests)

    print("\n===== FINAL RESULTS =====")
    print("LRU:", hit_ratio(lru_hits, len(requests)))
    print("LFU:", hit_ratio(lfu_hits, len(requests)))
    print("RL :", rl_hits / len(requests))


if __name__ == "__main__":
    main()