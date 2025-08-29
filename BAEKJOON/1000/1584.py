import heapq

N = int(input())
dangers = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
deads = [list(map(int, input().split())) for _ in range(M)]

zone = [[0] * 501 for _ in range(501)]
for x1, y1, x2, y2 in dangers:
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            zone[y][x] = -1

for x1, y1, x2, y2 in deads:
    for y in range(min(y1, y2), max(y1, y2) + 1):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            zone[y][x] = -2 

INF = float('inf')
dist = [[INF] * 501 for _ in range(501)]
dist[0][0] = 0

pq = [(0, [0, 0])]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

while pq:
    cost, node = heapq.heappop(pq)
    if cost != dist[node[0]][node[1]]:
        continue
    for i in range(4):
        if  0 <= node[0] + dy[i] <= 500 and 0 <= node[1] + dx[i] <= 500:
            y = node[0] + dy[i]
            x = node[1] + dx[i]
            if zone[y][x] == 0 :
                if cost < dist[y][x]:
                    dist[y][x] = cost
                    heapq.heappush(pq, (cost, [y, x]))
            elif zone[y][x] == -1 :
                if cost + 1 < dist[y][x]:
                    dist[y][x] = cost + 1
                    heapq.heappush(pq, (cost + 1, [y, x]))

if dist[500][500] == INF:
    print(-1)
else:
    print(dist[500][500])