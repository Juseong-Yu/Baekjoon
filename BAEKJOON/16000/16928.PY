from collections import deque

N, M = map(int, input().split())
board = [i for i in range(101)]
visited = [False] * 101
for n in range(N):
    start, end = map(int, input().split())
    board[start] = end

for m in range(M):
    start, end = map(int, input().split())
    board[start] = end

queue = deque()

queue.append((1, 0))
while queue:
    nowX, nowT = queue.popleft()
    if nowX == 100:
        result = nowT
        break
    else:
        for d in range(1, 7):
            if nowX + d <= 100:
                nextX = board[nowX + d]
                nextT = nowT + 1
                if visited[nextX] == False:
                    visited[nextX] = True
                    queue.append((nextX, nextT))

print(result)