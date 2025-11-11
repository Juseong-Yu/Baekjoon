R, C = map(int, input().split())
k = int(input())
obs = [list(map(int, input().split())) for _ in range(k)]
y, x = map(int, input().split())
dirs = list(map(int, input().split()))
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]
visited = [[False] * C for _ in range(R)]
visited[y][x] = True
for ob_y, ob_x in obs:
    visited[ob_y][ob_x] = True
dirnow = 0
while True:
    i = dirs[dirnow % 4]
    check_y = y + dy[i]
    check_x = x + dx[i]
    if 0 <= check_y < R and 0 <= check_x < C and visited[check_y][check_x] == False:
        y = check_y
        x = check_x
        visited[y][x] = True
    else:
        for _ in range(0, 3):
            dirnow += 1
            i = dirs[dirnow % 4]
            check_y = y + dy[i]
            check_x = x + dx[i]
            if 0 <= check_y < R and 0 <= check_x < C and visited[check_y][check_x] == False:
                break
        else:
            break
print(y, x)