import heapq

def prims(n, graph):
    visited = set()

    min_heap = [(0, 0)]  # (weight, node)

    mst_cost = 0

    while min_heap:

        weight, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)
        mst_cost += weight

        for nei, edge_weight in graph[node]:
            if nei not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, nei)
                )

    return mst_cost