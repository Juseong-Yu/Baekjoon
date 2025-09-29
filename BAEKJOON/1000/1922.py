def find(x):
    if parents[x] == x:
        return x
    
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    top_x = find(x)
    top_y = find(y)

    if rank[top_x] > rank[top_y]:
        parents[top_y] = top_x

    elif rank[top_y] > rank[top_x]:
        parents[top_x] = top_y

    else:
        rank[top_y] += 1
        parents[top_x] = top_y

N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))
    
edges.sort(key=lambda x : x[2])

cnt = 0
result = 0
for x, y, cost in edges:
    if find(x) == find(y) :
        continue

    union(x, y)
    result += cost
    if cnt == N - 1:
        break

print(result)