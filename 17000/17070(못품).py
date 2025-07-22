from collections import deque

N = int(input())
room = []
for _ in range(N):
    line = list(map(int, input().split()))
    room.append(line)

queue = deque([[0, 1, 1, 0]])
dp = []
result = 0
while len(queue) != 0:
    now = queue.popleft()
    if now[0] == N-1 and now[1] == N-1:
        result += now[2]

    if now[3] == 0:
        if now[1] < N - 1 :
            if room[now[0]][now[1] + 1] == 0:
                if [now[0], now[1] + 1, now[2] , 0] in dp:
                    idx = dp.index([now[0], now[1] + 1, now[2] , 0])
                    dp[idx] = [now[0], now[1] + 1, now[2] + 1 , 0]
                else:
                    queue.append([now[0], now[1] + 1, now[2] , 0])
                    dp.append([now[0], now[1] + 1, now[2] , 0])

        if now[0] < N - 1  and now[1] < N - 1:
            if room[now[0] + 1][now[1]] == 0 and room[now[0]][now[1] + 1] == 0 and room[now[0] + 1][now[1] + 1] == 0:
                if [now[0] + 1, now[1] + 1, now[2] , 2] in dp:
                    idx = dp.index([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp[idx] = [now[0] + 1, now[1] + 1, now[2] + 1 , 2]
                else:
                    queue.append([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp.append([now[0] + 1, now[1] + 1, now[2] , 2])


    if now[3] == 1:
        if now[0] < N - 1 :
            if room[now[0] + 1][now[1]] == 0:
                if [now[0] + 1, now[1], now[2] , 1] in dp:
                    idx = dp.index([now[0] + 1, now[1], now[2] , 1])
                    dp[idx] = [now[0] + 1, now[1], now[2] + 1 , 1]
                else:
                    queue.append([now[0] + 1, now[1], now[2] , 1])
                    dp.append([now[0] + 1, now[1], now[2] , 1])

        
        if now[0] < N - 1  and now[1] < N - 1:
            if room[now[0] + 1][now[1]] == 0 and room[now[0]][now[1] + 1] == 0 and room[now[0] + 1][now[1] + 1] == 0:
                if [now[0] + 1, now[1] + 1, now[2] , 2] in dp:
                    idx = dp.index([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp[idx] = [now[0] + 1, now[1] + 1, now[2] + 1 , 2]
                else:
                    queue.append([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp.append([now[0] + 1, now[1] + 1, now[2] , 2])



    if now[3] == 2:
        if now[1] < N - 1 :
            if room[now[0]][now[1] + 1] == 0:
                if [now[0], now[1] + 1, now[2] , 0] in dp:
                    idx = dp.index([now[0], now[1] + 1, now[2] , 0])
                    dp[idx] = [now[0], now[1] + 1, now[2] + 1 , 0]
                else:
                    queue.append([now[0], now[1] + 1, now[2] , 0])
                    dp.append([now[0], now[1] + 1, now[2] , 0])


        if now[0] < N - 1 :
            if room[now[0] + 1][now[1]] == 0:
                if [now[0] + 1, now[1], now[2] , 1] in dp:
                    idx = dp.index([now[0] + 1, now[1], now[2] , 1])
                    dp[idx] = [now[0] + 1, now[1], now[2] + 1 , 1]
                else:
                    queue.append([now[0] + 1, now[1], now[2] , 1])
                    dp.append([now[0] + 1, now[1], now[2] , 1])


        if now[0] < N - 1  and now[1] < N - 1:
            if room[now[0] + 1][now[1]] == 0 and room[now[0]][now[1] + 1] == 0 and room[now[0] + 1][now[1] + 1] == 0:
                if [now[0] + 1, now[1] + 1, now[2] , 2] in dp:
                    idx = dp.index([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp[idx] = [now[0] + 1, now[1] + 1, now[2] + 1 , 2]
                else:
                    queue.append([now[0] + 1, now[1] + 1, now[2] , 2])
                    dp.append([now[0] + 1, now[1] + 1, now[2] , 2])

print(result)