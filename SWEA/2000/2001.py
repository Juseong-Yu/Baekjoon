T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_result = 0
    for y in range(N - (M - 1) ):
        for x in range(N - (M - 1) ):
            for idx in range(3):
                for m in range(1, M):
                    result = 0
                    for y_smack in range(M):
                        for x_smack in range(M):
                            result += arr[y + y_smack][x + x_smack]
                    if result > max_result :
                        max_result = result
    print(f'#{t} {max_result}')