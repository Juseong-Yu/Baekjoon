T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nxn = [list(map(int, input().split())) for _ in range(N)]
    stack = [[0, 0, nxn[0][0]]]
    min_score = float('inf')
    while stack:
        now = stack.pop()
        y = now[0]
        x = now[1]
        if now[2] > min_score:
            continue
        if x == (N - 1) and y == (N - 1):
            if min_score > now[2]:
                min_score = now[2]
            continue
        if y + 1 < N:
            stack.append([y+1, x, now[2] + nxn[y + 1][x]])
        if x + 1 < N:
            stack.append([y, x + 1, now[2] + nxn[y][x + 1]])
    print(f'#{t} {min_score}')