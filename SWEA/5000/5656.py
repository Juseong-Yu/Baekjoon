from collections import deque
from copy import deepcopy

T = int(input())

def dfs(now, cnt):
    global min_result
    if cnt == N:
        result = 0
        for y in range(H):
            for x in range(W):
                if now[y][x] != 0:
                    result += 1

        if result < min_result:
            min_result = result
        
        return
        

    for i in range(W):
        next1 = bomb(now, i)
        if next1 == None:
            pass
        else:
            dfs(next1, cnt + 1)
        

def bomb(now, i):
    now_tmp = deepcopy(now)
    for y in range(H):
        if now_tmp[y][i] != 0:
            first_explode = (y, i)
            break
    else:
        return None

    queue = deque()
    queue.append(first_explode)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[False] * W for _ in range(H)]
    visited[first_explode[0]][first_explode[1]] = True

    while queue:
        explode = queue.popleft()
        distance = now_tmp[explode[0]][explode[1]]
        for j in range(1, distance):
            for l in range(4):
                if 0 <= explode[0] + dy[l] * j < H and 0 <= explode[1] + dx[l] * j < W and visited[explode[0] + dy[l] * j][explode[1] + dx[l] * j] == False:
                    queue.append((explode[0] + dy[l] * j , explode[1] + dx[l] * j))
                    visited[explode[0] + dy[l] * j][explode[1] + dx[l] * j] = True
    
    for y in range(H):
        for x in range(W):
            if visited[y][x] == True:
                now_tmp[y][x] = 0
    next = []
    for x in range(W):
        zero_cnt = 0
        line = []
        for y in range(H):
            if now_tmp[y][x] != 0:
                line.append(now_tmp[y][x])
            else:
                zero_cnt += 1
        line = [0] * zero_cnt + line
        next.append(line)
    next = list(zip(*next))
    next = list(map(list, next))
    return next

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_result = float('inf')
    dfs(bricks, 0)
    if min_result == float('inf'):
        print(f'#{t} {0}')
    else:
        print(f'#{t} {min_result}')
