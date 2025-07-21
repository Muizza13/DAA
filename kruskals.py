graph = {
    "A": {"B": 9, "C": 14, "D": 7},
    "B": {"A": 9, "C": 6, "D": 10, "E": 11},
    "C": {"A": 14, "B": 6, "F": 9},
    "D": {"A": 7, "B": 10, "E": 15},
    "E": {"B": 11, "F": 6},
    "F": {"C": 9, "E": 6},
}


def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]


def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if root1 != root2:
        parent[root2] = root1


def kruskal(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            if (neighbor, node, weight) not in edges:
                edges.append((node, neighbor, weight))
    edges.sort(key=lambda x: x[2])

    parent = {}
    for node in graph.keys():
        parent[node] = node

    mst = []

    for node1, node2, weight in edges:
        if find(parent, node1) != find(parent, node2):
            union(parent, node1, node2)
            mst.append((node1, node2, weight))

    return mst


mst_result = kruskal(graph)

print("Minimum Spanning Tree edges (Kruskal's, no OOP):")
total_weight = 0
for node1, node2, weight in mst_result:
    print(f"{node1} -- {node2} [{weight}]")
    total_weight += weight

print(f"Total weight of MST: {total_weight}")
