N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

visited = [False] * (N + 1)
cnt = 0
for idx in range(1, N + 1):
    if visited[idx] == False:
        stack = [idx]
        cnt += 1
        visited[idx] = True
        while stack:
            now = stack.pop()
            next = edges[now]
            for ele in next:
                if visited[ele] == False:
                    visited[ele] = True
                    stack.append(ele)
print(cnt)
