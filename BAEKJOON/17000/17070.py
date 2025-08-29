from collections import deque

N = int(input())
home = []
for _ in range(N):
    line = list(map(int, input().split()))
    home.append(line)

queue = deque()
# idx 0 y
# idx 1 x
# idx 2에 놓인 방향 - 0 == 가로 1 == 세로 2 == 대각선
# idx 3 거기까지 그 방향으로 갈수 있는 방법
queue.append([0, 1, 0])
