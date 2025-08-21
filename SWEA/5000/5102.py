from collections import deque

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V + 1)]

    for _ in range(E):
        node1, node2 = map(int, input().split())
        edges[node1].append(node2)
        edges[node2].append(node1)
    start, end = map(int, input().split())

    queue = deque()
    visited = [0] * (V + 1)
    visited[start] = 1
    queue.append(start)
    result = 0
    while queue:
        now = queue.popleft()
        if now == end:
            result = visited[now]
            break
        for next in edges[now]:
            if visited[next] == 0:
                queue.append(next)
                visited[next] = visited[now] + 1

    if result != 0:
        result -= 1
    print(f'#{t} {result}')