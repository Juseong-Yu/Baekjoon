def ABBA(arr, N, M):
    for y in range(N):
            for x in range(N - M + 1):
                for idx in range(M // 2):
                    check1 = x + idx
                    check2 = x + M - idx - 1
                    if arr[y][check1] != arr[y][check2]:
                        break
                else:
                    result = ''.join(arr[y][x : x + M])
                    return result
                  

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = ABBA(arr, N, M)
    if result == None:
        arr = list(zip(*arr))
        result = ABBA(arr, N, M)
    print(f'#{t} {result}')
