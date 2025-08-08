T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_result = 0
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            result_check = 0
            check_y = [1, 1, 0, 0]
            check_x = [0, 1, 1, 0]

            if result_check > max_result:
                max_result = result_check
            
    print(f'#{t} {max_result}')