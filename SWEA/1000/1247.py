T = int(input())
for t in range (1, T + 1):
    N = int(input())
    input_locs = list(map(int, input().split()))
    locs = []
    for idx in range(N + 2):
        locs.append((input_locs[idx * 2], input_locs[idx * 2 + 1]))
    office = locs[0]
    home = locs[1]
    client = locs[2:]

    visited = [False] * N
    min_dist = float('inf')
    def perm(idx, dist, loc):
        global min_dist
        if dist > min_dist:
            return
        if idx == N:
            next_dist = abs(loc[0] - home[0]) + abs(loc[1] - home[1])
            if min_dist > dist + next_dist:
                min_dist = dist + next_dist
            return
        
        for i in range(N):
            if visited[i] == False:
                visited[i] = True
                next_dist = abs(loc[0] - client[i][0]) + abs(loc[1] - client[i][1])
                perm(idx + 1, dist + next_dist, client[i])
                visited[i] = False

    perm(0, 0, office)
    print(f'#{t} {min_dist}')