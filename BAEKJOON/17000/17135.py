from itertools import combinations
import copy

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
archers = [i for i in range(M)]
archers = combinations(archers , 3)
max_score = 0

for archer in archers:
    score = 0
    enemys = copy.deepcopy(arr)
    for time in range(N):
        shoots = []
        for arrow in list(archer): # 각 궁수가 쏠 수 있는 적 확인
            #print(arrow)
            arrow_y = N
            arrow_x = arrow
            now_x = None
            now_y = None
            now_D = float("inf")
            for y in range(N - D, N):
                for x in range(arrow_x - D + 1, arrow_x + D ):
                    distance = (arrow_y - y) + abs(arrow_x - x)
                    #print(arrow, y, x, distance, time)
                    if x >= 0 and x < M and distance <= D and y >= 0 and enemys[y][x] == 1:
                        if now_D > distance:
                            now_x = x
                            now_y = y
                            now_D = distance
                        elif now_D == distance:
                            if now_x > x:
                                now_x = x
                                now_y = y
                                now_D = distance
            if now_D != float("inf"):
                shoots.append([now_y, now_x])
        for shoot in shoots:
            if enemys[shoot[0]][shoot[1]] == 1:
                score += 1
                enemys[shoot[0]][shoot[1]] = 0
        next_enemy = [[0] * M]
        next_enemy = next_enemy + enemys
        enemys = next_enemy
    if score > max_score:
        max_score = score
    
print(max_score)