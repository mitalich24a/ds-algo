def prims(n, graph):
    in_mst = [False] * n
    min_cost = [float('inf')] * n

    min_cost[0] = 0
    mst_cost = 0

    for _ in range(n):

        # Find minimum cost node not yet in MST
        node = -1
        for i in range(n):
            if not in_mst[i]:
                if node == -1 or min_cost[i] < min_cost[node]:
                    node = i

        # Add it to MST
        in_mst[node] = True
        mst_cost += min_cost[node]

        # Update neighbors
        for nei, wt in graph[node]:
            if not in_mst[nei]:
                min_cost[nei] = min(min_cost[nei], wt)

    return mst_cost
