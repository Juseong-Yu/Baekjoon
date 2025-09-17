from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    fields = [list(map(str, list(input()))) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if fields[y][x] == 'X':
                startX, startY = x, y
            if fields[y][x] == 'Y':
                endX, endY = x, y
    # 0 up 1 right 2 down 3 left
    queue = deque()
    queue.append((startX, startY, 0, 0, 0)) # x, y, direction, cut_cnt, move_cnt

    visited = [[[[False] * N for _ in range(N)] for _ in range(K + 1)] for _ in range(4)]
    visited[0][0][x][y] = True # direction, cut_cnt, x, y

    while queue:
        x, y, direction, cut_cnt, move_cnt  = queue.popleft()
        if x == endX and y == endY:
            print(f'#{t} {move_cnt}')
            break

        if direction == 0:
            next_y = y - 1
            next_x = x
            next_dir = [1, 3]
        elif direction == 1:
            next_x = x + 1
            next_y = y
            next_dir = [0, 2]
        elif direction == 2:
            next_y = y + 1
            next_x = x
            next_dir = [3, 1]
        elif direction == 3:
            next_x = x - 1
            next_y = y
            next_dir = [0, 2]
        if 0 <= next_y < N and 0 <= next_x < N:
            if fields[next_y][next_x] == 'T':
                if cut_cnt != K:
                    if visited[direction][cut_cnt + 1][next_x][next_y] == False:
                        queue.append((next_x, next_y, direction, cut_cnt + 1, move_cnt + 1))
                        visited[direction][cut_cnt + 1][next_x][next_y] = True
            else:
                if visited[direction][cut_cnt][next_x][next_y] == False:
                        queue.append((next_x, next_y, direction, cut_cnt, move_cnt + 1))
                        visited[direction][cut_cnt][next_x][next_y] = True

        for dir in next_dir:
            if visited[dir][cut_cnt][x][y] == False:
                queue.append((x, y, dir, cut_cnt, move_cnt + 1))
                visited[dir][cut_cnt][x][y] = True
    else:
        print(f'#{t} -1')