from heapq import heappop, heappush

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    min_e = [[float('inf')] * N for _ in range(N)]
    min_e[0][0] = 0
    pq = [(0, 0, 0)] # weight, y, x
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    while pq:
        w, y, x = heappop(pq)

        if min_e[y][x] < w:
            continue

        if y == N and x == N:
            break

        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                h_diff = heights[y + dy[i]][x + dx[i]] -  heights[y][x] 
                if h_diff < 0:
                    h_diff = 0
                if min_e[y + dy[i]][x + dx[i]] > min_e[y][x] + 1 + h_diff:
                    min_e[y + dy[i]][x + dx[i]] =  min_e[y][x] + 1 + h_diff
                    heappush(pq, (min_e[y][x] + 1 + h_diff, y + dy[i], x + dx[i]))

    print(f'#{t} {min_e[-1][-1]}')