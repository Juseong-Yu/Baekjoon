from collections import deque
T = int(input())
for t in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    queue = deque()
    result = set()
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    for y in range(4):
        for x in range(4):
            queue.append([y, x, str(board[y][x]), 1])

    while queue:
        now = queue.popleft()
        if now[3] == 7:
            result.add(now[2])
            continue

        for i in range(4):
            y = dy[i] + now[0]
            x = dx[i] + now[1]
            if 0 <= y < 4 and 0 <= x < 4:
                queue.append([y, x, now[2] + str(board[y][x]), now[3] + 1])
    
    print(f'#{t} {len(result)}')