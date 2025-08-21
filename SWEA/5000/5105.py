from collections import deque

T = int(input())
for t in range(1, T  + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    
    # 출발, 도착점 찾기
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start = (y, x)
                visited[y][x] = 1
            elif maze[y][x] == 3:
                end = (y, x)

    queue = deque()
    queue.append(start)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    result = 0
    while queue:
        now = queue.popleft()
        y = now[0]
        x = now[1]
        if maze[y][x] == 3:
            result = visited[y][x]
            break
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N:
                if maze[y + dy[i]][x + dx[i]] != 1 and visited[y + dy[i]][x + dx[i]] == 0:
                    queue.append((y + dy[i], x + dx[i]))
                    visited[y + dy[i]][x + dx[i]] = visited[y][x] + 1
    
    if result != 0:
        result -= 2
    print(f'#{t} {result}')
