N, M = map(int, input().split())
INF = float('inf')
dist = [INF] *  (N + 1) # 0번 노드는 안 씀
dist[1] = 0
edges = [list(map(int, input().split())) for _ in range(M)]
for _ in range(N - 1):
    for start, stop, cost in edges:
        if dist[start] != INF and dist[start] + cost < dist[stop]:
            dist[stop] = dist[start] + cost
        
for start, stop, cost in edges:
    if dist[start] != INF and dist[start] + cost < dist[stop]:
        print(-1)
        break

else:
    for ele in range(2, len(dist)):
        if dist[ele] == float('inf'):
            print(-1)
        else:
            print(dist[ele])

