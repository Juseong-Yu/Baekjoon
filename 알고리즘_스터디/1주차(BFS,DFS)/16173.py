from collections import deque
N = int(input())
queue = deque()
board = list(list(map(int, input().split())) for _ in range(N))

queue.append((0, 0))
visited = [[True] * N for _ in range(N)]
visited[0][0] = False
result = 'Hing'
while queue:
    now = queue.popleft()
    num = board[now[0]][now[1]]
    if num == -1:
        result = 'HaruHaru'
        break
    
    elif num == 0:
        continue
    else:
        if num + now[0] < N and visited[num + now[0]][now[1]]:
            visited[num + now[0]][now[1]] = True
            queue.append((num + now[0], now[1]))

        if num + now[1] < N and visited[now[0]][num + now[1]]:
            visited[now[0]][num + now[1]] = True
            queue.append((now[0], num + now[1]))
print(result)