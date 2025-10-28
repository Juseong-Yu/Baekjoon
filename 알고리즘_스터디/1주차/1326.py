from collections import deque

N = int(input())
arr = list(map(int, input().split()))
arr = [0] + arr
a, b = map(int, input().split())
queue = deque()
queue.append((a, 0))
visited = [False] * (N + 1)
while queue:
    now = queue.popleft()
    if now[0] == b:
        result = now[1]
        print(result)
        break
    if now[0] + arr[now[0]] <= N:
        for check in range(now[0] + arr[now[0]], N + 1, arr[now[0]]):
            if visited[check] == False:
                queue.append((check, now[1] + 1))
                visited[check] = True

    if 0 < now[0] - arr[now[0]]:
        for check in range(now[0] - arr[now[0]], 0, -arr[now[0]]):
            if visited[check] == False:
                queue.append((check, now[1] + 1))
                visited[check] = True
else:
    print(-1)
