from heapq import heappop, heappush

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    dist = [float('inf')] * (N + 1)
    dist[0] = 0
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges[start].append((weight, end))

    pq = [(0,  0)]

    while pq:
        w, e = heappop(pq)
        

        if dist[e] < w:
            continue

        if e == N:
            break
        
        else:
            for next_weight, next_node in edges[e]:
                if dist[next_node] > dist[e] + next_weight:
                    dist[next_node] = dist[e] + next_weight
                    heappush(pq, (dist[next_node], next_node))

    print(f'#{t} {dist[-1]}')