import heapq
N, M, K, S, T = map(int, input().split()) # 정점 수, 간선수, 주기상수, 출발사건, 도착사건 

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c, o = map(int, input().split())
    graph[u].append((v, c, o))

def dijkstra(graph, S, T):
    dist = [float('inf')] * (N + 1)
    dist[S] = 0
    
    pq = [(0, S)]
    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now]:
            continue
        for v, c, o in graph[now]:
            next_c = cost + c
            if next_c < dist[v] :
                if cost % o == 0:
                    dist[v] = next_c
                    heapq.heappush(pq, (next_c, v))
    
    return dist[T]

result = dijkstra(graph, S, T)
if result == float('inf'):
    print(-1)
else:
    print(result)