# 크루스칼로 가다가 집합이 2개일 때 반환
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
        return False
    
    if ranks[masterX] < masterY:
        parents[masterX] = masterY
    elif ranks[masterY] < masterX:
        parents[masterY] = masterX
    else:
        ranks[masterX] += 1
        parents[masterY] = masterX
    return True


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
ranks = [0] * (N + 1)
edges = []
for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x : x[2])

cnt = 0
min_weight = 0
for s, e, w in edges:
    if union(s, e):
        cnt += 1
        min_weight += w

        if cnt == (N - 2):
            break
if N == 2:
    print(0)
else:
    print(min_weight)