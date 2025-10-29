N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * (M) for _ in range(N)]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, -1, 1, -1, 1]
result = 0
for y in range(N):
    for x in range(M):
        if visited[y][x] == False:
            stack = [(y, x)]
            hight = board[y][x]
            visited[y][x] = True
            flag = True
            while stack:
                now_y, now_x = stack.pop()
                for i in range(8):
                    check_y = dy[i] + now_y
                    check_x = dx[i] + now_x
                    if 0 <= check_y < N and 0 <= check_x < M:
                        if hight == board[check_y][check_x] and visited[check_y][check_x] == False:
                            stack.append((check_y, check_x))
                            visited[check_y][check_x] = True
                        if hight < board[check_y][check_x]:
                            flag = False
            if flag == True:
                result += 1
            

print(result)