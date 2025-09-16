from heapq import heappop, heappush
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    roads = [list(map(int, list(input()))) for _ in range(N)]
    times = [[float('inf')] * N for _ in range(N)]
    times[0][0] = 0

    pq = [(0, 0, 0)] # w, y, x
    dy = [0, 0, -1, 1]
    dx = [1, -1 ,0, 0]

    while pq:
        w, y, x = heappop(pq)

        if times[y][x] < w:
            continue

        if y == N and x == N:
            break 

        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                if times[y + dy[i]][x + dx[i]] > roads[y + dy[i]][x + dx[i]] + w:
                    times[y + dy[i]][x + dx[i]] = roads[y + dy[i]][x + dx[i]] + w
                    heappush(pq, (times[y + dy[i]][x + dx[i]], y + dy[i], x + dx[i]))

    result = times[N - 1][N - 1]
    print(f'#{t} {result}')