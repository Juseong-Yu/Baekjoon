N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_val = float('inf')
def perm(i, val):
    global min_val
    if val > min_val:
        return

    if visited.count(False) == 1:
        if arr[i][0] == 0:
            return
        val_now = val + arr[i][0]
        if min_val > val_now:
            min_val = val_now
        return
    
    for j in range(1, N):
        if visited[j] == False:
            visited[j] = True
            if arr[i][j] != 0:
                perm(j, val + arr[i][j])
            visited[j] = False
perm(0,0)
print(min_val)