from collections import deque
N = int(input())
NxN = [[0] * N for _ in range(N)]

K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
for apple in apples:
    NxN[apple[0]- 1][apple[1] - 1] = 1

L = int(input())
moves = [list(input().split()) for _ in range(L)]
moves = deque(moves)

time = 0
snake = deque([(0, 0)]) # 왼쪽 끝 꼬리 오른쪽 끝 머리
direction = 1 # 오른 1 아래 2 왼 3 위 0
while True:
    time += 1
    # 머리 위치
    head = snake[-1]
    body = snake.copy()
    # 머리 움직이기
    if direction == 1:
        snake.append((head[0], head[1] + 1))

    if direction == 2:
        snake.append((head[0] + 1, head[1]))

    if direction == 3:
        snake.append((head[0], head[1] - 1))

    if direction == 0:
        snake.append((head[0] - 1, head[1]))

    # 머리 위치 바뀜
    head = snake[-1]
    # 게임 오버 확인
    if 0 <= head[0] < N and 0 <= head[1] < N and head not in body:
        pass
    else:
        break
    
    if NxN[head[0]][head[1]] == 1:
        NxN[head[0]][head[1]] = 0
    else:
        snake.popleft()

    if len(moves) != 0 and time == int(moves[0][0]):
        move = moves.popleft()
        move = move[1]
        if move == 'D':
            direction = (direction + 1) % 4
        elif move == 'L':
            if direction == 0:
                direction = 3
            else:
                direction = direction -1
print(time)