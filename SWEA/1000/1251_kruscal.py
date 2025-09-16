# 크루스칼 알고리즘
def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
def union(x, y):
    masterX = find(x)
    masterY = find(y)

    if masterX == masterY:
        return
    
    if ranks[masterX] < ranks[masterY]:
        parents[masterX] = masterY
    elif ranks[masterY] < ranks[masterX]:
        parents[masterY] = masterX
    else:
        ranks[masterX] += 1
        parents[masterY] = masterX

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    parents = [i for i in range(N)]
    ranks = [0] * N
    E = float(input())
    arr = list(zip(*arr))
    
    edges = []
    
    # 간선과 해당하는 거리를 모두 구해 저장
    for s in range(N):
        for e in range(s + 1, N):
            sx, sy = arr[s]
            ex, ey = arr[e]
            cost = ((sy - ey) ** 2 + (sx - ex) ** 2 ) * E
            edges.append((s, e, cost))
    edges.sort(key=lambda x : x[2])

    min_weight = 0
    cnt = 0
    
    for s, e, cost in edges:
        if find(s) != find(e):
            cnt += 1
            min_weight += cost
            union(s, e)

            if cnt == N - 1:
                break

    result = round(min_weight)
    print(f'#{t} {result}')