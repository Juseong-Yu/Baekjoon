import heapq

V, E = map(int, input().split())
K = int(input())

edges = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, dist = map(int, input().split())
    edges[start].append((end, dist))

INF = float('inf')
dists = [INF] * (V + 1)
pq = [(0, K)]
dists[K] = 0
while pq:
    dist, now = heapq.heappop(pq)

    for nxt, dist in edges[now]:
        if dists[now] + dist < dists[nxt]:
            dists[nxt] = dists[now] + dist
            heapq.heappush(pq,(dists[nxt], nxt))

for ele in dists[1:]:
    if ele == INF:
        print('INF')
    else:
        print(ele)