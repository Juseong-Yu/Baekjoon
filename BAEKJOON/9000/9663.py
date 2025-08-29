N = int(input())
visited = [False] * N
cnt = 0
arr = [i for i in range(N)]

def perm(idx, local_arr):
    global cnt
    
    if len(local_arr) != 0:
        last = local_arr[-1]
        for check_idx, check in enumerate(local_arr[:-1]):
            dist = idx - check_idx - 1
            if check + dist == last or check - dist == last:
                return
    if idx == N:
            cnt += 1
            return
    
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            perm(idx + 1, local_arr + [i])
            visited[i] = False

perm(0, [])

print(cnt)