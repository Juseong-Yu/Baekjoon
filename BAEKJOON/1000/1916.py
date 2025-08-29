import heapq

N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    start, stop, cost = map(int, input().split())
    edges[start].append([stop, cost])

A, B = map(int, input().split())
INF = float('inf')
dist = [INF] * (N + 1)
dist[A] = 0
pq = [(0, A)]

while pq:
    current_dist, node = heapq.heappop(pq)

    if current_dist > dist[node]:
        continue

    next = edges[node]
    for stop, cost in next:
        next_cost = cost + current_dist
        if next_cost < dist[stop]:
            dist[stop] = next_cost
            heapq.heappush(pq, (next_cost, stop))
print(dist[B])