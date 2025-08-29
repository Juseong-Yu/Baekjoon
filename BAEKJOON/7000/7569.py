from collections import deque

M, N, H = map(int, input().split()) # x, y, z 
tomatos = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

# 시작 토마토 위치 찾아서 큐에 넣기
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 1:
                queue.append((z, y, x))

dz = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dx = [-1, 1, 0, 0, 0, 0]
while queue:
    now = queue.popleft()
    z, y, x = now[0], now[1], now[2]
    for i in range(6):
        if 0 <= z + dz[i] < H and 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
            if tomatos[z + dz[i]][y + dy[i]][x + dx[i]] == 0:
                queue.append((z + dz[i], y + dy[i], x + dx[i]))
                tomatos[z + dz[i]][y + dy[i]][x + dx[i]] = tomatos[z][y][x] + 1

result = 1
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatos[z][y][x] == 0:
                result = 0
                break

            if tomatos[z][y][x] > result:
                result = tomatos[z][y][x]
        if result == 0:
            break
    if result == 0:
        break

print(result - 1)