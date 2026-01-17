from collections import deque
n, m = map(int, input().split())
board = []
result = [[-1] * m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j, ele in enumerate(line):
        if ele == 2:
            queue = deque()
            queue.append((i, j, 0))
            result[i][j] = 0
        elif ele == 0:
            result[i][j] = 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
while queue:
    y, x, t = queue.popleft()
    for i in range(4):
        if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n:
            if result[y + dy[i]][x + dx[i]] == -1:
                result[y + dy[i]][x + dx[i]] = t + 1
                queue.append((y + dy[i], x + dx[i], t + 1))

for line in result:
    for ele in line:
        print(ele, end=' ')
    print()