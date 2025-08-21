from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

queue = deque()
queue.append((0, 0))
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while queue:
    now = queue.popleft()
    if now == (N - 1, M - 1):
        print(visited[N-1][M-1])
        break

    for i in range(4):
        if 0 <= now[0] + dy[i] < N and 0 <= now[1] + dx[i] < M:
            if visited[now[0] + dy[i]][now[1] + dx[i]] == 0 and maze[now[0] + dy[i]][now[1] + dx[i]] == 1:
                queue.append((now[0] + dy[i], now[1] + dx[i]))
                visited[now[0] + dy[i]][now[1] + dx[i]] = visited[now[0]][now[1]] + 1
