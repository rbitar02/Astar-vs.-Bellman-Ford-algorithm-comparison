# bellman_ford.py

from typing import Any, Dict, Tuple
from graph import Graph
import time

def bellman_ford(graph: Graph, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Any], Dict[str, Any]]:
    """
    Bellman-Ford single-source shortest paths.

    Returns:
        dist:   shortest distance from source to each node
        parent: predecessor of each node on its shortest path
        metrics: dictionary with runtime, relaxation count, negative_cycle flag
    """
    dist: Dict[Any, float] = {}
    parent: Dict[Any, Any] = {}

    # initialization
    for node in graph.nodes():
        dist[node] = float("inf")
        parent[node] = None
    dist[source] = 0.0

    num_nodes = len(graph.nodes())
    relaxations = 0
    negative_cycle = False

    start_time = time.perf_counter()

    # main relaxation loop: repeat |V|-1 times
    for _ in range(num_nodes - 1):
        updated = False
        for u, v, w in graph.edges:
            relaxations += 1
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        # early stop if nothing changed in this pass
        if not updated:
            break

    # check for negative cycles reachable from source
    for u, v, w in graph.edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            negative_cycle = True
            break

    end_time = time.perf_counter()

    metrics = {
        "runtime_seconds": end_time - start_time,
        "relaxations": relaxations,
        "negative_cycle": negative_cycle,
    }

    return dist, parent, metrics
