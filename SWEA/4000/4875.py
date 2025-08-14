T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for t in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                start = [y,x]
            elif miro[y][x] == 3:
                finish = [y,x]
    stack = [start]
    visited[start[0]][start[1]] = True
    result = 0
    while stack :
        #print(stack)
        now = stack.pop()
        for i in range(4):
            next = [now[0] + dy[i], now[1] + dx[i]]
            if 0 <= next[0] < N and 0 <= next[1] < N and visited[next[0]][next[1]] == False:
                if next == finish:
                    result = 1
                    break
                if miro[next[0]][next[1]] == 0:
                    stack.append(next)
                    visited[next[0]][next[1]] = True
    print(f'#{t} {result}')