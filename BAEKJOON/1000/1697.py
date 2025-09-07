from collections import deque
N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))
visited = [False] * 200001

while queue:
    now, cnt = map(int, queue.popleft())
    visited[now] = True
    if now < 0:
        continue
    if now == K:
        print(cnt)
        break
    else:
        if now + 1 < 200000 and visited[now + 1] == False:
            queue.append((now + 1, cnt + 1))
        if now > 0 and visited[now - 1] == False:
            queue.append((now - 1, cnt + 1))
        if now * 2 < 200000 and visited[now * 2] == False:
            queue.append((now * 2, cnt + 1))
