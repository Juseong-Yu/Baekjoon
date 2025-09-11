T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * (N + 1)
    min_cost = float('inf')

    def perm(idx, cost):
        global min_cost
        if idx == N:
            if min_cost > cost:
                min_cost = cost
            return
        if cost > min_cost:
            return
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                perm(idx + 1, cost + arr[idx][i])
                visited[i] = False
    
    perm(0, 0)
    print(f'#{t} {min_cost}')
