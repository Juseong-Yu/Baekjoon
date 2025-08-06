from collections import deque

for t in range(1, 11):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    indegree = [0] * (V + 1)
    graph = [[] for _ in range (V + 1)]
    for idx in range(0, len(arr), 2):
        start = arr[idx]
        stop = arr[idx + 1]
        graph[start].append(stop)
        indegree[stop] += 1
    queue = deque()
    for idx in range(1, V + 1):
        if indegree[idx] == 0:
            queue.append(idx)
    
    result = []
    while queue:
        now = queue.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    print(f'#{t}', end = ' ')
    result = list(map(str, result))
    result = ' '.join(result)
    print(result)