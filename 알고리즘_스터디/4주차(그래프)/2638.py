from collections import deque
N , M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

flag = False
result = 0
while flag == False:
    flag = True
    result += 1
    queue = deque()
    queue.append((0, 0))
    while queue:
        now_y , now_x = queue.popleft()
        for i in range(4):
            if 0 <= now_y + dy[i] < N and 0 <= now_x + dx[i] < M:
                if farm[now_y + dy[i]][now_x + dx[i]] == 0:
                    queue.append((now_y + dy[i], now_x + dx[i]))
                    farm[now_y + dy[i]][now_x + dx[i]] = -1
                elif farm[now_y + dy[i]][now_x + dx[i]] == 1:
                    farm[now_y + dy[i]][now_x + dx[i]] += 1
                elif farm[now_y + dy[i]][now_x + dx[i]] == 2:
                    farm[now_y + dy[i]][now_x + dx[i]] = -1

    for y in range(N):
        for x in range(M):
            if farm[y][x] == -1:
                farm[y][x] = 0
            elif 1 <= farm[y][x] <= 2:
                farm[y][x] = 1
                flag = False
print(result)