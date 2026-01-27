N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
stack = []
for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            stack.append((y, x))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
cnt = 0
while stack:
    nowY, nowX = stack.pop()
    for i in range(4):
        if 0 <= nowY + dy[i] < N and 0 <= nowX + dx[i] < M:
            if campus[nowY + dy[i]][nowX + dx[i]] == "O":
                stack.append((nowY + dy[i], nowX + dx[i]))
                campus[nowY + dy[i]][nowX + dx[i]] = "X"

            elif campus[nowY + dy[i]][nowX + dx[i]] == "P":
                stack.append((nowY + dy[i], nowX + dx[i]))
                campus[nowY + dy[i]][nowX + dx[i]] = "X"
                cnt += 1

if cnt == 0:
    print('TT')
else:
    print(cnt)