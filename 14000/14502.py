from itertools import combinations
from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
lab = [list(map(int, input().split()))for _ in range(N)]

emptys = []
viruses = []
empty_count = 0
# 벽 세우기 가능한 위치 찾기
for y in range(N):
    for x in range(M):
        if lab[y][x] == 0:
            emptys.append((y, x))
            empty_count += 1
        if lab[y][x] == 2:
            viruses.append((y, x))

emptys = combinations(emptys, 3)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

min_virus = float('inf')
for empty in emptys:
    now_lab = deepcopy(lab)
    queue = deque()
    queue.extend(viruses)
    for wall in empty:
        now_lab[wall[0]][wall[1]] = 1

    virus_count = 0
    while queue:
        now = queue.popleft()
        y, x = now[0], now[1]
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M:
                if now_lab[y + dy[i]][x + dx[i]] == 0:
                    queue.append((y + dy[i], x + dx[i]))
                    now_lab[y + dy[i]][x + dx[i]] = 2
                    virus_count += 1

    if min_virus > virus_count:
        min_virus = virus_count

print(empty_count - min_virus - 3)