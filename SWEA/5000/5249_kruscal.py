# 크루스칼 알고리즘

def find(x):
    if parents[x] == x:
        return parents[x]
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
    V, E = map(int, input().split())
    parents = [i for i in range(V + 1)]
    ranks = [0] * (V + 1)
    edges = []
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((start, end, weight))

    edges.sort(key=lambda x : x[2])

    cnt = 0
    min_weight = 0
    for s, e, w in edges:
        if find(s) == find(e):
            pass
        else:
            cnt += 1
            min_weight += w
            union(s, e)

            if cnt == V: # 0번부터 V번까지 존재하므로 갯수는 V + 1개, 크루스칼에서 종료조건으로는 V
                break

    print(f'#{t} {min_weight}')