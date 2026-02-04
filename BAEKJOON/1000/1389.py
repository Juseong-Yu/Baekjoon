from collections import deque
N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
result = []
for _ in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)
for n in range(1, N + 1):
    bacon = [-1] * (N + 1)
    bacon[0] = 0
    queue = deque()
    queue.append((n, 0))
    while queue:
        now, degree = queue.popleft()
        for node in edges[now]:
            if bacon[node] == -1:
                bacon[node] = degree + 1
                queue.append((node, degree + 1))
    result.append(sum(bacon))
minbacon = 10000000
for idx, ele in enumerate(result):
    if ele < minbacon:
        minidx = idx + 1
        minbacon = ele

print(minidx)