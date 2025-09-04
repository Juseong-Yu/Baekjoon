N = int(input())
garden = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [0, 0, 1, -1, 1, 1, -1, -1, 2, -2, 0, 0]
dx = [1, -1, 0, 0, -1, 1, 1, -1, 0, 0, -2, 2]

min_cost = float('inf')
def comb(cnt, score):
    global min_cost
    if cnt == 3:
        if score < min_cost:
            min_cost = score
        return
    
    for y in range(1, N - 1):
        for x in range(1, N - 1):
            if visited[y][x] == False:
                # 심으면 안되는 곳 검사
                flag = False
                for i in range(12):
                    if 0 < dy[i] + y < N and 0 < dx[i] + x < N and visited[dy[i] + y][dx[i] + x ] == True:
                        flag = True
                        break
                    if flag:
                        break
                if not flag:
                    visited[y][x] = True
                    next_score = score + garden[y][x] + garden[y+1][x] + garden[y][x + 1] + garden[y-1][x] + garden[y][x- 1]
                    comb(cnt + 1, next_score)
                    visited[y][x] = False

comb(0, 0)
print(min_cost)