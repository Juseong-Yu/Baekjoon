from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    
    queue = deque()
    queue.append((R, C, 1))
    cnt = 1
    while queue:
        now = queue.popleft()
        r, c, time = map(int, now)
        if time == L:
            continue
        tunnel = underground[r][c]
        if 0 <= (r -1):
            check = underground[r - 1][c]
            if (check == 1 or check == 2 or check == 5 or check == 6) and (tunnel == 1 or tunnel == 2 or tunnel == 4 or tunnel == 7) and visited[r-1][c] == False:
                cnt += 1
                queue.append((r-1, c, time + 1))
                visited[r-1][c] = True

        if r + 1 < N:
            check = underground[r + 1][c]
            if (check == 1 or check == 2 or check == 4 or check == 7) and (tunnel == 1 or tunnel == 2 or tunnel == 5 or tunnel == 6) and visited[r + 1][c] == False:
                cnt += 1
                queue.append((r + 1, c, time + 1))
                visited[r+1][c] = True

        if 0 <= c - 1:
            check = underground[r][c - 1]
            if (check == 1 or check == 3 or check == 4 or check == 5) and (tunnel == 1 or tunnel == 3 or tunnel == 6 or tunnel == 7) and visited[r][c-1] == False:
                cnt += 1
                queue.append((r, c-1, time + 1))
                visited[r][c-1] = True

        if c + 1 < M:
            check = underground[r][c + 1]
            if (check == 1 or check == 3 or check == 6 or check == 7) and (tunnel == 1 or tunnel == 3 or tunnel == 4 or tunnel == 5) and visited[r][c+1] == False:
                cnt += 1
                queue.append((r, c+1, time + 1))
                visited[r][c + 1] = True
    print(f'#{t} {cnt}')