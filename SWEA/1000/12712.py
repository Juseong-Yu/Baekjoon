T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    bugs = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 십자가
    ys = [0, 0, 1, -1]
    xs = [1, -1, 0, 0]
    for y in range(N):
        for x in range(N):
            check = 0
            for i in range(1, M):
                for j in range(0, 4):
                    check_y = y + (ys[j] * i)
                    check_x = x + (xs[j] * i)
                    if 0 <= check_y < N and 0 <= check_x < N:
                        check += bugs[check_y][check_x]
            check += bugs[y][x]
            if check > result:
                result = check

    # 대각선
    ys = [1, -1, 1, -1]
    xs = [1, -1, -1, 1]
    
    for y in range(N):
        for x in range(N):
            check = 0
            for i in range(1, M):
                for j in range(0, 4):
                    check_y = y + (ys[j] * i)
                    check_x = x + (xs[j] * i)
                    if 0 <= check_y < N and 0 <= check_x < N:
                        check += bugs[check_y][check_x]
            check += bugs[y][x]
            if check > result:
                result = check
    print(f'#{t} {result}')
