T = int(input())
for t in range(1, T + 1):
    N = int(input())
    
    dp = [[0] * N for _ in range(N)]
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    arr = [(y, x) for y in range(N) for x in range(N)]
    rooms = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    max_cnt = 0
    max_start = 0
    while arr:
        now = arr.pop()
        y = now[0]
        x = now[1]
        if visited[y][x] == False:
            cnt = 1
            go_stack = []
            back_stack = []
            start = rooms[y][x]
            for i in range(4):
                if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and visited[y + dy[i]][x + dx[i]] == False:
                    if rooms[y + dy[i]][x + dx[i]] == rooms[y][x] - 1:
                        go_stack = [(y + dy[i], x + dx[i])]
                        visited[y + dy[i]][x + dx[i]] = True
                        cnt += 1
                    elif rooms[y + dy[i]][x + dx[i]] == rooms[y][x] + 1:
                        back_stack = [(y + dy[i], x + dx[i])]
                        cnt += 1
                        visited[y + dy[i]][x + dx[i]] = True

            while back_stack:
                back_now = back_stack.pop()
                back_y = back_now[0]
                back_x = back_now[1]
                
                for i in range(4):
                    if 0 <= back_y + dy[i] < N and 0 <= back_x + dx[i] < N and visited[back_y + dy[i]][back_x + dx[i]] == False:
                        if rooms[back_y + dy[i]][back_x + dx[i]] == rooms[back_y][back_x] + 1:
                            back_stack.append((back_y + dy[i], back_x + dx[i]))
                            visited[back_y + dy[i]][back_x + dx[i]] = True
                            cnt += 1
                            

            while go_stack:
                go_now = go_stack.pop()
                go_y = go_now[0]
                go_x = go_now[1]
                start = rooms[go_y][go_x]
                for i in range(4):
                    if 0 <= go_y + dy[i] < N and 0 <= go_x + dx[i] < N and visited[go_y + dy[i]][go_x + dx[i]] == False:
                        if rooms[go_y + dy[i]][go_x + dx[i]] == rooms[go_y][go_x] - 1:
                            go_stack.append((go_y + dy[i], go_x + dx[i]))
                            visited[go_y + dy[i]][go_x + dx[i]] = True
                            cnt += 1
        if max_cnt == cnt:
            if start < max_start:
                max_cnt = cnt
                max_start = start
        elif max_cnt < cnt:
            max_cnt = cnt
            max_start = start
    print(f'#{t} {max_start} {max_cnt}')