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

def find(x):
    if parents[x] == x:
        return parents[x]
    
    else:
        parents[x] = find(parents[x])
        return parents[x]


V, E = map(int, input().split())
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x : x[2])
parents = [i for i in range(V + 1)]
ranks = [0] * (V + 1)

cnt = 0
min_weight = 0
for edge in edges:
    s, e, w = edge
    if find(s) != find(e):
        union(s, e)
        min_weight += w
        cnt += 1

        if cnt == (V - 1):
            break

print(min_weight)