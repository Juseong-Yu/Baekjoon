N, D = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N)]

dist = [i for i in range(D + 1)]
for idx in range(1, D + 1):
    dist[idx] = dist[idx - 1] + 1
    for edge in edges:
        start = edge[0]
        end = edge[1]
        cost = edge[2]
        if end == idx and dist[end] - dist[start] > cost:
            dist[end] = dist[start] + cost
        
print(dist[-1])