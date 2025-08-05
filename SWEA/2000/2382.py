T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    box = [[[]for _ in range(N)] for _ in range(N)]
    germs = []
    for _ in range(K): 
        germ = list(map(int, input().split())) # 세로 가로 수 이동방법
        germs.append(germ)
    for time in range(1, M + 1):
        box = [[[]for _ in range(N)] for _ in range(N)]
        for germ in germs:
            counts = germ[2]
            move = germ[3]
            if move == 1:
                germ[0] -= 1
            elif move == 2:
                germ[0] += 1
            elif move == 3:
                germ[1] -= 1
            elif move == 4:
                germ[1] += 1
            
            y = germ[0]
            x = germ[1]
            if x == 0 or x == (N - 1) or y == 0 or y == (N - 1):
                if move == 1:
                    move = 2
                    counts = counts //2
                elif move == 2:
                    move = 1
                    counts = counts //2
                elif move == 3:
                    move = 4
                    counts = counts //2
                elif move == 4:
                    move = 3
                    counts = counts //2
            box[y][x].append([counts, move]) # 수 이동방법
        germs = []
        for y in range(N):
            for x in range(N):
                if box[y][x]:
                    if len(box[y][x]) == 1:
                        ele = box[y][x][0]
                        counts = ele[0]
                        move = ele[1]
                        germs.append([y,x,counts, move])
                    else:
                        max_counts = 0
                        max_move = None
                        total_counts = 0
                        for idx, ele in enumerate(box[y][x]):
                            total_counts += ele[0]
                            if ele[0] > max_counts:
                                max_move = ele[1]
                                max_counts = ele[0]
                        germs.append([y, x, total_counts, max_move])
    result = 0
    for germ in germs:
        result += germ[2]
    print(f'#{t} {result}')