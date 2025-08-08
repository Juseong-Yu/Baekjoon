from copy import deepcopy

TC = int(input())
for t in range(TC):
    N, M, W = map(int, input().split())

    roads = [list(map(int, input().split())) for _ in range(M)]
    worms = [list(map(int, input().split())) for _ in range(W)]
    
    for idx in range(W):
        worms[idx][2] = - worms[idx][2]

    tmp_road = deepcopy(roads)
    for road in tmp_road:
        roads.append([road[1], road[0], road[2]])

    edges = roads + worms
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    flag = False
    for _ in range(N - 1):
        for start, stop, cost in edges:
            if dist[start] != INF and dist[stop] > dist[start] + cost:
                dist[stop] = dist[start] + cost

    for start, stop, cost in edges:
        if dist[start] != INF and dist[stop] > dist[start] + cost:
            print('YES')
            flag = True

    if flag == False:
        print('NO')