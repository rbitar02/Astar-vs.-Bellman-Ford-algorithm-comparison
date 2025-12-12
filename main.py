# main.py
from graph import Graph
from bellman_ford import bellman_ford
from astar import astar, zero_heuristic

def has_negative_edge(graph: Graph) -> bool:
    for u, v, w in graph.edges:
        if w < 0:
            return True
    return False

def print_bf_goal(dist_bf, goal, negative_cycle):
    if negative_cycle:
        print("  dist[goal] = undefined (negative cycle detected)")
        return

    if goal not in dist_bf:
        print("  dist[goal] = (goal node not in graph)")
        return

    val = dist_bf[goal]
    if val == float("inf"):
        print("  dist[goal] = inf (no path)")
    else:
        print("  dist[goal] =", val)

def run_test(name, graph, start, goal):
    print("=" * 60)
    print(f"TEST: {name}")
    print(f"Start: {start}  Goal: {goal}")
    print("-" * 60)

    # Bellman-Ford
    dist_bf, parent_bf, metrics_bf = bellman_ford(graph, start)
    print("Bellman-Ford:")
    print_bf_goal(dist_bf, goal, metrics_bf["negative_cycle"])
    print("  negative_cycle =", metrics_bf["negative_cycle"])
    print("  relaxations =", metrics_bf["relaxations"])
    print("  runtime_seconds =", metrics_bf["runtime_seconds"])
    print()

    # A*
    if has_negative_edge(graph):
        print("A*: Skipped (negative edges not allowed).")
    else:
        _, _, metrics_a = astar(graph, start, goal, zero_heuristic)
        print("A* (zero heuristic):")
        if metrics_a["path_cost"] == float("inf"):
            print("  path_cost = inf (no path)")
        else:
            print("  path_cost =", metrics_a["path_cost"])
        print("  path =", metrics_a["path"])
        print("  nodes_expanded =", metrics_a["nodes_expanded"])
        print("  pq_ops =", metrics_a["pq_ops"])
        print("  runtime_seconds =", metrics_a["runtime_seconds"])

    print("=" * 60)
    print()

# -------------------------
# Test Graph Builders
# -------------------------

def build_test1_basic():
    g = Graph()
    g.add_directed_edge("A", "B", 1)
    g.add_directed_edge("B", "C", 2)
    g.add_directed_edge("A", "C", 5)
    g.add_directed_edge("C", "D", 1)
    g.add_directed_edge("B", "D", 5)
    g.add_directed_edge("A", "D", 10)
    return g

def build_test2_equal_paths():
    g = Graph()
    g.add_directed_edge("A", "B", 2)
    g.add_directed_edge("A", "C", 2)
    g.add_directed_edge("B", "D", 2)
    g.add_directed_edge("C", "D", 2)
    g.add_directed_edge("A", "D", 5)
    return g

def build_test3_negative_edge():
    g = Graph()
    g.add_directed_edge("S", "A", 1)
    g.add_directed_edge("A", "B", -2)
    g.add_directed_edge("B", "T", 2)
    g.add_directed_edge("S", "T", 5)
    return g

def build_test4_negative_cycle():
    g = Graph()
    g.add_directed_edge("S", "A", 1)
    g.add_directed_edge("A", "B", 1)
    g.add_directed_edge("B", "A", -3)
    return g

def build_test5_no_path():
    g = Graph()
    g.add_directed_edge("S", "A", 2)
    g.add_directed_edge("A", "B", 2)
    g.adj["T"] = []

    return g

# -------------------------
# Main
# -------------------------

def main():
    # Test 1
    graph1 = build_test1_basic()
    run_test("1 - Basic correctness (expected cost=4, path A-B-C-D)", graph1, "A", "D")

    # Test 2
    graph2 = build_test2_equal_paths()
    run_test("2 - Equal-cost shortest paths (expected cost=4)", graph2, "A", "D")

    # Test 3
    graph3 = build_test3_negative_edge()
    run_test("3 - Negative edge (no cycle) (BF works, A* skipped)", graph3, "S", "T")

    # Test 4
    graph4 = build_test4_negative_cycle()
    run_test("4 - Negative cycle (BF detects, A* skipped)", graph4, "S", "B")

    # Test 5
    graph5 = build_test5_no_path()
    run_test("5 - No path exists (expected dist=inf, path=[])", graph5, "S", "T")

if __name__ == "__main__":
    main()
