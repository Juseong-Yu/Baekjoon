T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flags = [list(input()) for _ in range(N)]

    white_all = []
    blue_all = []
    red_all = []

    for flag in flags:
        white = 0
        blue = 0
        red = 0
        for ele in flag:
            if ele == 'W':
                blue += 1
                red += 1
            elif ele == 'B':
                white += 1
                red += 1
            elif ele == 'R':
                white += 1
                blue += 1
        white_all.append(white)
        blue_all.append(blue)
        red_all.append(red)
    min_result = float('inf')

    for white in range(0, N - 2):
        white_chage = sum(white_all[0:white + 1])
        for blue in range(white + 1, N - 1):
            blue_chage = sum(blue_all[white + 1:blue + 1])
            red = N - 1
            red_change = sum(red_all[blue + 1:red + 1])
            result = white_chage + blue_chage + red_change
            if min_result > result:
                min_result = result



    print(f'#{t} {min_result}')