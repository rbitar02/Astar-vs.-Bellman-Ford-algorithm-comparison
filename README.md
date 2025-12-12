# CIS 505 Term Project – Item 1 (A* vs Bellman–Ford)

This project implements and compares two shortest-path algorithms:

- **A\*** (A-Star) — shortest path from a start node to a goal node (non-negative edge weights only)
- **Bellman–Ford** — single-source shortest paths that supports negative edge weights and detects negative cycles

The project includes:
- Graph data structure
- Implementations of both algorithms
- Automated execution of test cases
- Printed metrics for comparison (runtime, relaxations, nodes expanded, etc.)

---

## Files

- `main.py` – runs the test cases and prints results + metrics
- `graph.py` – directed weighted graph (adjacency list + edge list)
- `astar.py` – A* implementation + path reconstruction
- `bellman_ford.py` – Bellman–Ford implementation + negative cycle detection
- `requirements.txt` – no external dependencies (standard library only)

---

## Requirements

- Python 3.x (recommended: 3.9+)
- No external libraries required

If using a virtual environment:

### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate
