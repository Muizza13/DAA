graph = {
    "A": {"B": 9, "C": 14, "D": 7},
    "B": {"A": 9, "C": 6, "D": 10, "E": 11},
    "C": {"A": 14, "B": 6, "F": 9},
    "D": {"A": 7, "B": 10, "E": 15},
    "E": {"B": 11, "F": 6},
    "F": {"C": 9, "E": 6},
}


def prim(graph, start):
    visited = set()
    mst = []
    visited.add(start)

    edges = []
    for to, weight in graph[start].items():
        edges.append((weight, start, to))

    while edges:
        edges.sort()
        weight, frm, to = edges.pop(0)

        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for next_to, next_weight in graph[to].items():
                if next_to not in visited:
                    edges.append((next_weight, to, next_to))

    return mst


# Run Prim's algorithm
result = prim(graph, "A")

print("Edges in MST:")
total_weight = 0
for frm, to, weight in result:
    print(f"{frm} -- {to} [{weight}]")
    total_weight += weight

print(f"Total weight of MST: {total_weight}")
