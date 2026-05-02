import matplotlib.pyplot as plt
import csv
from cache.lru import LRUCache
from cache.lfu import LFUCache
from rl.environment import CacheEnv
from rl.agent import QAgent
from utils.parser import load_requests, normalize_requests


def run_lru(requests, size):
    cache = LRUCache(size)
    hits = 0
    for r in requests:
        if cache.get(r):
            hits += 1
        else:
            cache.put(r)
    return hits / len(requests)


def run_lfu(requests, size):
    cache = LFUCache(size)
    hits = 0
    for r in requests:
        if cache.get(r):
            hits += 1
        else:
            cache.put(r)
    return hits / len(requests)


def run_rl(requests, size):
    env = CacheEnv(size, requests)
    agent = QAgent(size)

    # -------- TRAIN --------
    for _ in range(200):
        state = env.reset()
        done = False

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state)
            state = next_state

        agent.decay_epsilon()

    # -------- EVALUATE --------
    state = env.reset()
    done = False
    hits = 0

    while not done:
        action = agent.act(state)
        next_state, reward, done = env.step(action)

        if reward > 0:
            hits += 1

        state = next_state

    return hits / len(requests)


def main():
    raw = load_requests("data/apache_logs", 10000)
    requests = normalize_requests(raw)

    sizes = [2, 5, 10, 20]

    lru_res, lfu_res, rl_res = [], [], []

    for size in sizes:
        print(f"Testing cache size {size}")
        lru_res.append(run_lru(requests, size))
        lfu_res.append(run_lfu(requests, size))
        rl_res.append(run_rl(requests, size))

    # save results
    with open("results/cache_size_results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Cache Size", "LRU", "LFU", "RL"])
        for i in range(len(sizes)):
            writer.writerow([sizes[i], lru_res[i], lfu_res[i], rl_res[i]])

    # plot
    plt.plot(sizes, lru_res, label="LRU")
    plt.plot(sizes, lfu_res, label="LFU")
    plt.plot(sizes, rl_res, label="RL")

    plt.xlabel("Cache Size")
    plt.ylabel("Hit Ratio")
    plt.legend()
    plt.title("Cache Size vs Hit Ratio")

    plt.savefig("plots/cache_size.png")
    plt.show()


if __name__ == "__main__":
    main()