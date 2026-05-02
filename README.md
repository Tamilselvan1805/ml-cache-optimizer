# 🚀 ML Cache Optimizer

An advanced system that compares traditional cache eviction strategies (LRU, LFU) with a Reinforcement Learning (RL)–based adaptive approach using real-world web traffic.

---

## 📌 Overview

Caching is critical for reducing latency and improving system performance.
Traditional policies like **LRU** and **LFU** are efficient but static.

This project introduces an **ML-based adaptive cache eviction strategy** that:

* Learns from request patterns
* Adapts dynamically
* Competes with optimal heuristics

---

## 🧠 Key Features

* ✅ LRU (Least Recently Used) implementation
* ✅ LFU (Least Frequently Used) implementation
* ✅ Reinforcement Learning–based cache policy
* ✅ Hybrid RL + LFU optimization
* ✅ Real-world dataset (Apache logs)
* ✅ Experimentation with cache size & workload
* ✅ Performance visualization (graphs)

---

## ⚙️ Tech Stack

* Python
* NumPy
* Matplotlib
* Reinforcement Learning (Q-Learning)

---

## 📂 Project Structure

```bash
ml-cache-optimizer/
│
├── cache/                # LRU & LFU implementations
├── rl/                   # RL environment + agent
├── utils/                # parser + metrics
├── experiments/          # evaluation scripts
├── plots/                # generated graphs
├── results/              # CSV outputs
├── data/                 # Apache logs dataset
│
├── main.py               # main execution
├── config.py             # configuration
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

* Apache HTTP Logs
* Represents real-world request patterns
* Exhibits strong **frequency locality**

---

## 🧪 Experiments

### 1. Cache Size vs Hit Ratio

* Cache sizes tested: `2, 5, 10, 20`
* Measures scalability

### 2. Workload Size vs Performance

* Requests tested: `5K, 10K, 20K`
* Measures stability

---

## 📈 Results

### Final Hit Ratios

| Algorithm | Hit Ratio |
| --------- | --------- |
| LRU       | 0.083     |
| LFU       | 0.2023    |
| RL        | 0.1929    |

---

## 📉 Graphs

### Cache Size vs Hit Ratio

![Cache Size](plots/cache_size.png)

### Workload vs Performance

![Workload](plots/workload.png)

---

## 🔍 Insights

* Performance increases with cache size for all algorithms
* LFU consistently outperforms others due to strong frequency locality
* RL closely approximates LFU and improves as cache size increases
* Workload size has minimal impact due to stable request distribution
* RL generalizes well across different workloads
* Cache capacity is the dominant factor influencing hit ratio

---

## 🧠 Key Learnings

* Reinforcement Learning can model system-level optimization
* Proper evaluation (train vs test separation) is critical
* Hybrid ML + heuristic approaches are highly effective

---

## ▶️ How to Run

```bash
# install dependencies
pip install -r requirements.txt

# run main comparison
python main.py

# run experiments
python -m experiments.cache_size_test
python -m experiments.workload_test
```

---

## 📁 Output

* Graphs saved in: `plots/`
* Results saved in: `results/`

---

## 🚀 Future Improvements

* Deep RL using neural networks (DQN)
* Latency-aware caching simulation
* Distributed caching systems
* Real-time adaptive cache tuning

---

## 💼 Resume Highlight

> Designed and evaluated an ML-based adaptive cache eviction system using reinforcement learning on real-world web logs, achieving near-optimal performance compared to LFU.

---

## 👤 Author

**Tamil Chandru**

---

## ⭐ If you like this project

## Give it a star ⭐ and feel free to fork!
