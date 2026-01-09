from pprint import pprint
from collections import deque
from copy import deepcopy
K, N1, M1, N2, M2 = map(int, input().split())
A, B = map(int, input().split())
Gsize1 = A * B
Gsize2 = A * B
R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
hole1 = []
hole2 = []
for k in range(K):
    d, dr, dc = map(int, input().split())
    if d == 1:
        hole1.append((dr, dc))
    else:
        hole2.append((dr, dc))

board1 = [[0] * M1 for _ in range(N1)]
board2 = [[0] * M2 for _ in range(N2)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 게이트 저장 (게이트 = G)
for a in range(A):
    for b in range(B):
        board1[R1 + a][C1 + b] = 'G'
        board2[R2 + a][C2 + b] = 'G'

# 블랙홀 저장 (블랙홀 = B)
for dr, dc in hole1:
    if board1[dr][dc] == 'G':
        Gsize1 -= 1
    board1[dr][dc] = 'B'

for dr, dc in hole2:
    if board2[dr][dc] == 'G':
        Gsize2 -= 1
    board2[dr][dc] = "B"

# y좌표, x좌표, 차원, 시간, 통로에 있는 시간
queue = deque()
queue.append((0, 0, 1, 0, 0))
time = 0
result = 'hing...'
visited1 = [[[False] * M1 for _ in range(N1)] for _ in range(3)]
visited2 = [[[False] * M2 for _ in range(N2)] for _ in range(3)]
while queue:
    y, x, d, t1, t2 = queue.popleft()
    # 내 위치가 블랙홀이면 안됨
    if d == 1 and t2 == 0:
        if board1[y][x] == 'B':
            continue
    elif d == 2:
        if board2[y][x] == 'B':
            continue

    # 똑같은 경우의 수를 똑같은 시간에 했었으면 안됨
    if d == 1:
        if visited1[t2][y][x] == True:
            continue
        else:
            visited1[t2][y][x] = True
    elif d == 2:
        if visited2[t2][y][x] == True:
            continue
        else:
            visited2[t2][y][x] = True

    print(y, x, d, t1, t2)
    # 만약 둘 중 한개의 게이트가 막히면, 넘어가는거 불가능
    if (Gsize2 == 0 or Gsize1 == 0) and d == 1 and t2 == 0:
        continue

    # 시간이 한번 가면 블랙홀을 만들어주어야 한다. visited 를 추가한다.
    if time != t1:
        #pprint(board1)
        #pprint(board2)
        print('next')
        time = t1
        nexthole1 = []
        nexthole2 = []
        visited1 = [[[False] * M1 for _ in range(N1)] for _ in range(3)]
        visited2 = [[[False] * M2 for _ in range(N2)] for _ in range(3)]
        for blacky, blackx in hole1:
            if blacky == N1 - 1 and blackx == 0:
                if board1[0][0] == 'G':
                    Gsize1 -= 1
                board1[0][0] = 'B'
                nexthole1.append((0, 0))
            elif blacky % 2 == 0:
                if blackx == M1-1:
                    if board1[blacky + 1][blackx] == 'G':
                        Gsize1 -= 1
                    board1[blacky + 1][blackx] = 'B'
                    nexthole1.append((blacky + 1, blackx))
                else:
                    if board1[blacky][blackx + 1] == 'G':
                        Gsize1 -= 1
                    board1[blacky][blackx + 1] = 'B'
                    nexthole1.append((blacky, blackx + 1))
            elif blacky % 2 == 1:
                if blackx == 0:
                    if board1[blacky + 1][blackx] == 'G':
                        Gsize1 -= 1
                    board1[blacky + 1][blackx] = 'B'
                    nexthole1.append((blacky + 1, blackx))
                else:
                    if board1[blacky][blackx -1] == 'G':
                        Gsize1 -= 1
                    board1[blacky][blackx -1] = 'B'
                    nexthole1.append((blacky, blackx - 1))

        for blacky, blackx in hole2:
            if blacky == N2 - 1 and blackx == 0:
                if board2[0][0] == 'G':
                    Gsize2 -= 1
                board2[0][0] = 'B'
                nexthole2.append((0, 0))
            elif blacky % 2 == 0:
                if blackx == M2 - 1:
                    if board2[blacky + 1][blackx] == 'G':
                        Gsize2 -= 1
                    board2[blacky + 1][blackx] = 'B'
                    nexthole2.append((blacky + 1, blackx))
                else:
                    if board2[blacky][blackx + 1] == 'G':
                        Gsize2 -= 1
                    board2[blacky][blackx + 1] = 'B'
                    nexthole2.append((blacky, blackx + 1))
            elif blacky % 2 == 1:
                if blackx == 0:
                    if board2[blacky + 1][blackx] == 'G':
                        Gsize2 -= 1
                    board2[blacky + 1][blackx] = 'B'
                    nexthole2.append((blacky + 1, blackx))
                else:
                    if board2[blacky][blackx -1] == 'G':
                        Gsize2 -= 1
                    board2[blacky][blackx -1] = 'B'
                    nexthole2.append((blacky, blackx - 1))
        # 탈출 전에 우주선이 블랙홀에 먹히면 끝남
        if board2[N2 - 1][M2 - 1] == 'B':
            #print('NOOOO')
            continue

        hole1 = deepcopy(nexthole1)
        hole2 = deepcopy(nexthole2)

    # 도착하면 탈출 다만 블랙홀은 아니여야 함 
    if y == N2-1 and x == M2-1 and d == 2:
        if board2[y][x] == 'B':
            break
        else:
            result = time
            break

    if d == 1:
        if board1[y][x] == 'B' and t2 == 0:
            continue
        else:
            if board1[y][x] == 'G':
                if t2 == 2:
                    goY = R2 + (y - R1)
                    goX = C2 + (x - C1)
                    queue.append((goY, goX, 2, t1+1, 0))
                elif t2 == 1:
                    queue.append((y, x, 1, t1+1, 2))
                else:
                    queue.append((y, x, 1, t1+1, 1))
                    for i in range(4):
                        if 0 <= y+dy[i] < N1 and 0 <= x + dx[i] < M1:
                            queue.append((y+dy[i], x + dx[i], 1, t1+1, 0))
            else:
                for i in range(4):
                    if 0 <= y+dy[i] < N1 and 0 <= x + dx[i] < M1:
                        queue.append((y+dy[i], x + dx[i], 1, t1+1, 0))
    elif d == 2:
        for i in range(4):
            if 0 <= y+dy[i] < N2 and 0 <= x + dx[i] < M2:
                queue.append((y+dy[i], x + dx[i], 2, t1+1, 0))

pprint(board2)
print(Gsize1, Gsize2)
print(result)