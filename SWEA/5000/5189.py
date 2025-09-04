T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    loc = [i for i in range(1, N + 1)]
    visited = [False] * (N + 1)
    visited[1] = True
    min_score = float('inf')
    def perm(cnt, before, score):
        global min_score
        if cnt == N:
            score += cost[before - 1][0]
            if min_score > score:
                min_score = score
            return
        for next in loc:
            if visited[next] == False:
                visited[next] = True
                perm(cnt + 1, next, score + cost[before - 1][next - 1])
                visited[next] = False
    perm(1, 1, 0)
    print(f'#{t} {min_score}')