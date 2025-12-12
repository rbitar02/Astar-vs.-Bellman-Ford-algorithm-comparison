# astar.py
from typing import Any, Dict, Tuple, Callable
from graph import Graph
import heapq
import time

Heuristic = Callable[[Any, Any], float]

def zero_heuristic(node: Any, goal: Any) -> float:
    """Default heuristic: always 0 (A* behaves like Dijkstra)."""
    return 0.0

def reconstruct_path(parent: Dict[Any, Any], start: Any, goal: Any):
    """Rebuild path from start to goal using parent pointers."""
    path = []
    current = goal
    while current is not None:
        path.append(current)
        if current == start:
            break
        current = parent.get(current)
    path.reverse()
    # if start is not at the beginning, there was no path
    if not path or path[0] != start:
        return []
    return path

def astar(graph: Graph,
          start: Any,
          goal: Any,
          heuristic: Heuristic = zero_heuristic) -> Tuple[Dict[Any, float], Dict[Any, Any], Dict[str, Any]]:
    """
    A* single-pair shortest path from start to goal.

    Returns:
        g:       cost from start to each visited node
        parent:  predecessor of each node on its path
        metrics: dictionary with runtime, nodes_expanded, pq_ops, path_cost, path
    """
    # g-score: best known distance from start
    g: Dict[Any, float] = {node: float("inf") for node in graph.nodes()}
    parent: Dict[Any, Any] = {node: None for node in graph.nodes()}
    g[start] = 0.0

    # open set as priority queue: (f, tie_breaker, node)
    open_heap = []
    counter = 0
    start_h = heuristic(start, goal)
    heapq.heappush(open_heap, (start_h, counter, start))

    in_open = {start}
    closed = set()

    nodes_expanded = 0
    pq_ops = 1  # initial push

    start_time = time.perf_counter()

    while open_heap:
        f_current, _, current = heapq.heappop(open_heap)
        pq_ops += 1  # popped from heap

        if current in closed:
            continue

        closed.add(current)
        nodes_expanded += 1

        if current == goal:
            break

        for neighbor, weight in graph.neighbors(current):
            if neighbor in closed:
                continue

            tentative_g = g[current] + weight
            if tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parent[neighbor] = current
                counter += 1
                f_neighbor = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f_neighbor, counter, neighbor))
                pq_ops += 1
                in_open.add(neighbor)

    end_time = time.perf_counter()

    path = reconstruct_path(parent, start, goal)
    path_cost = g[goal] if path else float("inf")

    metrics = {
        "runtime_seconds": end_time - start_time,
        "nodes_expanded": nodes_expanded,
        "pq_ops": pq_ops,
        "path": path,
        "path_cost": path_cost,
    }

    return g, parent, metrics
