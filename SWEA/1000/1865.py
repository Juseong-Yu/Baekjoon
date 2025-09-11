T = int(input())
for t in range(1, T + 1):
    N = int(input())
    input_arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [[0] * N for _ in range(N)]

    visited = [False] * (N + 1)
    max_perc = 0

    for y in range(N):
        for x in range(N):
            arr[y][x] = [input_arr[y][x], x]

    for y, line in enumerate(arr):
        arr[y] = sorted(line, reverse=True)


    def perm(idx, perc):
        global max_perc
        if idx == N:
            if max_perc < perc:
                max_perc = perc
            return
        
        if max_perc > perc:
            return
        
        for val, i in arr[idx]:
            if visited[i] == False:
                visited[i] = True
                perm(idx + 1, perc * (val / 100))
                visited[i] = False
        return
    perm(0, 1)
    result = round(max_perc * 100, 6)
    print(f'#{t} {result:.6f}')