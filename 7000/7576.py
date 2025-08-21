from collections import deque

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 1:
            queue.append((y, x))

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
while queue:
    now = queue.popleft()
    y, x = now[0], now[1]

    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
            if tomatos[y + dy[i]][x + dx[i]] == 0:
                queue.append((y + dy[i], x + dx[i]))
                tomatos[y + dy[i]][x + dx[i]] = tomatos[y][x] + 1

max_result = 1
for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 0:
            max_result = 0
            break
        elif tomatos[y][x] > max_result:
            max_result = tomatos[y][x]
    if max_result == 0:
        break

print(max_result - 1)