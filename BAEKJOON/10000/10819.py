N = int(input())
A = list(map(int, input().split()))
visited = [False] * (N)
idxs = [i for i in range(N)]
path = []

max_result = 0
def perm(cnt):
    global max_result
    if cnt == N:
        result = 0
        for idx in range(N - 1):
            result += abs(path[idx] - path[idx+1])
        if result > max_result:
            max_result = result
        return
    
    for idx in idxs:
        if visited[idx] == False:
            visited[idx] = True
            path.append(A[idx])
            perm(cnt + 1)
            path.pop()
            visited[idx] = False
perm(0)
print(max_result)