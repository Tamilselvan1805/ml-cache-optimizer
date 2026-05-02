import matplotlib.pyplot as plt
import csv
from cache.lru import LRUCache
from cache.lfu import LFUCache
from rl.environment import CacheEnv
from rl.agent import QAgent
from utils.parser import load_requests, normalize_requests


def run_algo(cache_class, requests, size):
    cache = cache_class(size)
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

    # TRAIN
    for _ in range(200):
        state = env.reset()
        done = False

        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state)
            state = next_state

        agent.decay_epsilon()

    # EVALUATE
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
    sizes = [5000, 10000, 20000]
    cache_size = 5

    lru_res, lfu_res, rl_res = [], [], []

    for s in sizes:
        raw = load_requests("data/apache_logs", s)
        requests = normalize_requests(raw)

        print(f"Testing workload size {s}")

        lru_res.append(run_algo(LRUCache, requests, cache_size))
        lfu_res.append(run_algo(LFUCache, requests, cache_size))
        rl_res.append(run_rl(requests, cache_size))

    with open("results/workload_results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Workload", "LRU", "LFU", "RL"])
        for i in range(len(sizes)):
            writer.writerow([sizes[i], lru_res[i], lfu_res[i], rl_res[i]])

    plt.plot(sizes, lru_res, label="LRU")
    plt.plot(sizes, lfu_res, label="LFU")
    plt.plot(sizes, rl_res, label="RL")

    plt.xlabel("Workload Size")
    plt.ylabel("Hit Ratio")
    plt.legend()
    plt.title("Workload vs Performance")

    plt.savefig("plots/workload.png")
    plt.show()


if __name__ == "__main__":
    main()