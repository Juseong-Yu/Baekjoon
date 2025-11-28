# 가장 최소 비용 경로를 구한 후, 그것들을 한번 씩 부숴 가장 큰 값을 구해본다. 

import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

def dijkstra_find(graph):
    dist = [[float('inf'), [i]] for i in range(N + 1)]
    dist[1][0] = 0
    pq = [(0, 1)]

    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now][0]:
            continue
            
        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt][0]:
                dist[nxt][0] = new_cost
                dist[nxt][1] = dist[now][1] + [nxt]
                heapq.heappush(pq, (new_cost, nxt))
    
    return dist[-1][1]

def dijkstra_get(graph, x, y):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]

    while pq:
        cost, now = heapq.heappop(pq)
        if cost > dist[now]:
            continue
        
        for nxt, w in graph[now]:
            if now == x and nxt == y:
                continue
            if nxt == y and now == x:
                continue
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
    return dist[-1]

best_way = dijkstra_find(graph)
result = 0
for i in range(len(best_way)-1):
    check = dijkstra_get(graph, best_way[i], best_way[i + 1])
    if check > result:
        result = check

print(result)