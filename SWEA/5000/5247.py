from collections import deque

T = int(input())

for t in range(1, T + 1):
    visited = [False] * 1000001
    N, M = map(int, input().split())
    queue = deque([[N, 0]])
    visited[N] = True
    while queue:
        now_data = queue.popleft()
        now, cnt = now_data[0], now_data[1]
        if now == M:
            result = cnt
            break
        if now - 10 >= M:
            nexts = [now - 10]
        elif now > M:
            nexts = [now - 1]
        else:
            nexts = [now - 10, now - 1, now + 1, now * 2]

        for next in nexts:
            if 0 < next <= 1000000:
                if visited[next] == False:
                    visited[next] = True
                    queue.append([next, cnt + 1])
    
    print(f'#{t} {result}')