from collections import deque
import sys

input = sys.stdin.readline
dy = [0, 0, -1, 1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        grounds = [list(map(int, input().split())) for _ in range(h)]
        cnt = 0

        for y in range(h):
            for x in range(w):
                if grounds[y][x] == 1 :
                    cnt += 1
                    queue = deque()
                    queue.append((y, x))
                    grounds[y][x] = 2
                    while queue:
                        now = queue.popleft()
                        for i in range(8):
                            next_y = dy[i] + now[0]
                            next_x = dx[i] + now[1]
                            if 0 <= next_y < h and 0 <= next_x < w:
                                if grounds[next_y][next_x] == 1:
                                    grounds[next_y][next_x] = 2
                                    queue.append((next_y, next_x))

    print(cnt)