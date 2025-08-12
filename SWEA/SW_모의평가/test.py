T = int(input())
for t in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [[0] * n for _ in range(4)]
    for time in range(1, k + 1):
        for y in range(4):
            for x in range(n):
                if (y + x + 1) % time == 0:
                    if arr[y][x] == 1:
                        arr[y][x] = 0
                    elif arr[y][x] == 0:
                        arr[y][x] = 1
    result = 0
    for y in range(4):
        for x in range(n):
            if arr[y][x] == 1:
                result +=1
    
    print(f'#{t} {result}')

