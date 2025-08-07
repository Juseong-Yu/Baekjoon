for t in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for idx in range(100):
        if ladder[99][idx] == 2:
            now_x = idx
    now_y = 99
    move = 1 # 1 위, 2 우, 3 왼
    while True:
        if move == 1: # 위로 올라가는 경우
            now_y -= 1
            if now_y == 0:
                break
            elif now_x - 1 >= 0 and ladder[now_y][now_x - 1] == 1:
                move = 3
            elif now_x + 1 <= 99 and ladder[now_y][now_x + 1] == 1:
                move = 2

        elif move == 2:
            now_x += 1
            if ladder[now_y - 1][now_x] == 1:
                move = 1

        elif move == 3:
            now_x -= 1
            if ladder[now_y - 1][now_x] == 1:
                move = 1
    print(f'#{t} {now_x}')
        
        