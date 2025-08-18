T = int(input())
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for y in range(N):
        for x in range(N):
            score = 0
            for i in range(1, N):
                for j in range(4):
                    if 0 <= y + dy[j] * i < N and 0 <= x + dx[j] * i < N:
                        score += arr[y + dy[j] * i][x + dx[j] * i]
            score += arr[y][x]
            if max_score < score:
                max_score = score
    print(f'#{t} {max_score}')