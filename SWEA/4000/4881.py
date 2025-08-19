T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    permut = [i for i in range(N)]
    visited = [False] * (N + 1)
    min_val = float('inf')
    def permu(idx, val):
        global min_val
        if val > min_val:
            return
        
        if idx == (N):
            if val < min_val:
                min_val = val
            return
        
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                permu(idx + 1, val + arr[idx][i])
                visited[i] = False
    permu(0,0)
    print(f'#{t} {min_val}')