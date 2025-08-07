T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(N):
        counter = 0
        for x in range(N):
            if box[y][x] == 1:
                counter += 1
            elif box[y][x] == 0:
                counter = 0
            if counter == K:
                result += 1
            elif counter == K + 1:
                result -= 1
    for x in range(N):
        counter = 0
        for y in range(N):
            if box[y][x] == 1:
                counter += 1
            elif box[y][x] == 0:
                counter = 0
            if counter == K:
                result += 1
            elif counter == K + 1:
                result -= 1
    print(f'#{t} {result}')