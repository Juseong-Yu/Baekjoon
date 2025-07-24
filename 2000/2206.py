from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road_map = []
for _ in range(N):
    line = list(map(int,list(input().strip())))
    road_map.append(line)

bfs = deque()
bfs.append([0, 0, False, 1])
visited = set()
while True:
    if len(bfs) == 0:
        print(-1)
        break
    now = bfs.popleft()
    if now[0] == N-1 and now[1] == M-1:
        print(now[3])
        break
    checker = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if now[2] == False:
        for check in checker:
            if (N > now[0] + check[0] >= 0) and (M > now[1] + check[1] >= 0) and ((now[0] + check[0], now[1] + check[1], False) not in visited):
                if road_map[now[0] + check[0]][now[1] + check[1]] == 1:
                    bfs.append([now[0] + check[0], now[1] + check[1], True, now[3] + 1 ])
                    visited.add((now[0] + check[0], now[1] + check[1], True))
                else:
                    bfs.append([now[0] + check[0], now[1] + check[1], False, now[3] + 1 ])
                    visited.add((now[0] + check[0], now[1] + check[1],False))
    
    if now[2] == True:
        for check in checker:
            if N > now[0] + check[0] >= 0 and M > now[1] + check[1] >= 0 and (now[0] + check[0], now[1] + check[1], True) not in visited:
                if road_map[now[0] + check[0]][now[1] + check[1]] == 1:
                    pass
                else:
                    bfs.append([now[0] + check[0], now[1] + check[1], True, now[3] + 1 ])
                    visited.add((now[0] + check[0], now[1] + check[1],True))