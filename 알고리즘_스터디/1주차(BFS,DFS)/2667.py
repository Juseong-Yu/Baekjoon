N = int(input())
board = list(list(map(int, list(input()))) for _ in range(N))
visited = [[False] * N for _ in range(N)]
houses = []
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and visited[y][x] == False:
            cnt = 1
            visited[y][x] = True
            stack = [(y, x)]
            while stack:
                now = stack.pop()
                now_y = now[0]
                now_x = now[1]
                for i in range(4):
                    check_y = dy[i] + now_y
                    check_X = dx[i] + now_x
                    if 0 <= check_y < N and 0 <= check_X < N:
                        if board[check_y ][check_X] == 1 and visited[check_y][check_X] == False:
                            visited[check_y][check_X] = True
                            stack.append((check_y, check_X))
                            cnt += 1

            houses.append(cnt)

houses.sort()
print(len(houses))
for ele in houses:
    print(ele)