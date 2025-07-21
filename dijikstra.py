graph = {
    "A": {"B": 9, "C": 14, "D": 7},
    "B": {"A": 9, "C": 6, "D": 10, "E": 11},
    "C": {"A": 14, "B": 6, "F": 9},
    "D": {"A": 7, "B": 10, "E": 15},
    "E": {"B": 11, "F": 6},
    "F": {"C": 9, "E": 6},
}


def dijikstra(graph, source):
    unvisited = set(graph.keys())
    infinity = float("inf")

    distance = {node: infinity for node in graph}
    distance[source] = 0

    while unvisited:
        current = min((node for node in unvisited), key=lambda node: distance[node])

        unvisited.remove(current)

        for neighbour, weight in graph[current].items():
            if neighbour in unvisited:
                newDistance = distance[current] + weight
                if newDistance < distance[neighbour]:
                    distance[neighbour] = newDistance

    return distance


source = "A"
result = dijikstra(graph, source)
print(f"Source is {source}")
for key, value in result.items():
    print(f"{key}: {value}")
