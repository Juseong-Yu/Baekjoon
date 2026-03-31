import heapq

N, E = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((c, b))
    edges[b].append((c, a))

v1, v2 = map(int, input().split())
INF = float("inf")

def dijkstra(start, end, edges):
    dists = [INF] * (N + 1)
    dists[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dists[node] < dist:
            continue
        
        for next_dist, next_node in edges[node]:
            if dists[next_node] > next_dist + dist:
                dists[next_node] = next_dist + dist
                heapq.heappush(pq, (next_dist + dist, next_node))

    return dists[end]

one = dijkstra(1, v1, edges) + dijkstra(v1, v2, edges) + dijkstra(v2, N , edges)
two = dijkstra(1, v2, edges) + dijkstra(v2, v1, edges) + dijkstra(v1, N , edges)

if min(one, two) == INF:
    print(-1)
else:
    print(min(one, two))