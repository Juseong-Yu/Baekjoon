T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    arr = [[0] * N for _ in range(N)]
    move = 1
    y = 0
    x = 0
    for num in range(1, N * N + 1):
        arr[y][x] = num
        if move == 1:
            if 0 <= x + 1 < N and arr[y][x + 1] == 0:
                x += 1
                
            else:
                move = 2
                y += 1

        elif move == 2:
            if 0 <= y + 1 < N and arr[y+1][x] == 0:
                y += 1

            else:
                move = 3
                x -= 1

        elif move == 3:
            if 0 <= x + 1 < N and arr[y][x - 1] == 0:
                x -= 1

            else:
                move = 4
                y -= 1

        elif move == 4:
            if 0 <= y + 1 < N and arr[y - 1][x] == 0:
                y -= 1

            else:
                move = 1
                x += 1

    for idx in range(N):
        print(' '.join(map(str,arr[idx])))