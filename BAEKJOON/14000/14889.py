N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]
visited = [False] * (N)
min_diff = float('inf')
path = []

def comb(cnt, now):
    global min_diff
    if cnt == N / 2:
        start = path
        link = list(set(people) - set(start))
        score1 = 0
        score2 = 0
        for start_i in range(N // 2):
            for start_j in range(start_i  + 1, N // 2):
                score1 += arr[start[start_i]][start[start_j]] + arr[start[start_j]][start[start_i]]
        
        for link_i in range(N // 2):
            for link_j in range(link_i , N // 2):
                score2 += arr[link[link_i]][link[link_j]] + arr[link[link_j]][link[link_i]]
        
        score_diff = abs(score1 - score2)
        if score_diff < min_diff:
            min_diff = score_diff

    for idx in range(now + 1, N):
        if visited[idx] == False:
            visited[idx] = True
            path.append(idx)
            comb(cnt + 1, idx)
            visited[idx] = False
            path.pop()
comb(0, 0)
print(min_diff)