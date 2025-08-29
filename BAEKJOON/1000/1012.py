T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, input().split())
    veges = [list(map(int, input().split())) for _ in range(K)]
    lands = [[0] * M for _ in range(N)]
    for x, y in veges:
        lands[y][x] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    for y in range(N):
        for x in range(M):
            if lands[y][x] == 1:
                result += 1
                stack = [[y, x]]
                while stack:
                    now = stack.pop()
                    check_y = now[0]
                    check_x = now[1]
                    lands[check_y][check_x] = 0
                    for i in range(4):
                        if 0 <= check_y + dy[i] < N and 0 <= check_x + dx[i] < M:
                            if lands[check_y + dy[i]][check_x + dx[i]] == 1:
                                stack.append([check_y + dy[i], check_x + dx[i]])
    print(result)

