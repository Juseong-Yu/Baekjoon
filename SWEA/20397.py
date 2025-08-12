T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    rocks = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for check in range(1, j + 1):
            if (i + check) < N and (i - check) >= 0:
                if rocks[i + check] == rocks[i - check]:
                    if rocks[i + check] == 1:
                        rocks[i + check] = 0
                        rocks[i - check] = 0
                    elif rocks[i + check] == 0:
                        rocks[i + check] = 1
                        rocks[i - check] = 1
    result = list(map(str, rocks))
    result = ' '.join(result)
    print(f'#{t} {result}')