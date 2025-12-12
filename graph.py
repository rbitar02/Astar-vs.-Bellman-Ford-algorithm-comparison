# graph.py
from typing import Dict, List, Tuple, Any

class Graph:
    """Directed weighted graph using adjacency list + edge list."""
    def __init__(self) -> None:
        # node -> list of (neighbor, weight)
        self.adj: Dict[Any, List[Tuple[Any, float]]] = {}
        # flat list of edges for Bellman-Ford
        self.edges: List[Tuple[Any, Any, float]] = []

    def add_directed_edge(self, u: Any, v: Any, w: float) -> None:
        """Add a directed edge u -> v with weight w."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []  
        self.adj[u].append((v, w))
        self.edges.append((u, v, w))

    def nodes(self) -> List[Any]:
        """Return list of nodes in the graph."""
        return list(self.adj.keys())

    def neighbors(self, u: Any) -> List[Tuple[Any, float]]:
        """Return neighbors of u as (v, weight)."""
        return self.adj.get(u, [])
