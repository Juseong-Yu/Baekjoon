N = int(input())
board = [list(input()) for _ in range(N)]

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]
cnt1 = 0
cnt2 = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for y in range(N):
    for x in range(N):
        if visited1[y][x] == False:
            cnt1 += 1
            stack = [(y, x)]
            color = board[y][x]
            while stack:
                nowY, nowX = stack.pop()
                for i in range(4):
                    if 0 <= nowY + dy[i] < N and 0 <= nowX + dx[i] < N:
                        if board[nowY + dy[i]][nowX + dx[i]] == color and visited1[nowY + dy[i]][nowX + dx[i]] == False:
                            stack.append((nowY + dy[i], nowX + dx[i]))
                            visited1[nowY + dy[i]][nowX + dx[i]] = True

for y in range(N):
    for x in range(N):
        if visited2[y][x] == False:
            cnt2 += 1
            stack = [(y, x)]
            color = board[y][x]
            if color == 'G' or color == 'R':
                color = ['G', 'R']
            while stack:
                nowY, nowX = stack.pop()
                for i in range(4):
                    if 0 <= nowY + dy[i] < N and 0 <= nowX + dx[i] < N:
                        if board[nowY + dy[i]][nowX + dx[i]] in color and visited2[nowY + dy[i]][nowX + dx[i]] == False:
                            stack.append((nowY + dy[i], nowX + dx[i]))
                            visited2[nowY + dy[i]][nowX + dx[i]] = True

print(cnt1, cnt2)