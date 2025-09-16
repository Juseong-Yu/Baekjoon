# 프림 알고리즘
from heapq import heappop, heappush
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges[n1].append((w, n2))
        edges[n2].append((w, n1))

    pq = [(0, 1)]
    MST = [False] * (V + 1)
    min_weight = 0

    while pq:
        weight, node = heappop(pq)
        if MST[node]:
            continue

        MST[node] = True
        min_weight += weight

        for next_weight, next_node in edges[node]:
            if MST[next_node]:
                continue
            else:
                heappush(pq, (next_weight, next_node))

    print(f'#{t} {min_weight}')
