from collections import deque

for t in range(1, 11):
    T = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]

    start = (1,1)
    end = (13,13)
    queue = deque()
    queue.append(start)
    visited = [[0] * 16 for _ in range(16)]
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    result = 0
    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]
        if y == end[0] and x == end[1]:
            result = 1
            break
        for i in range(4):
            if 0 <= y + dy[i] < 16 and 0 <= x + dx[i] < 16:
                if visited[y + dy[i]][x + dx[i]] == 0 and maze[y + dy[i]][x + dx[i]] != 1:
                    visited[y + dy[i]][x + dx[i]] = visited[y][x] + 1
                    queue.append((y + dy[i], x + dx[i]))
    print(f'#{t} {result}')
