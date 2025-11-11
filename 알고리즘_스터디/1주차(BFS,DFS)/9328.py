T = int(input())
for t in range (T):
    h, w = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    keys = set(input())
    stack = []
    result = 0
    doors = {}
    visited = [[False] * w for _ in range(h)]

    def func(ele, y, x):
        global stack
        global visited
        global result
        global keys
        global building
        global doors
        if visited[y][x] == False:
            if ele == '.':
                stack.append((y, x))
                visited[y][x] = True
            elif ele == '$':
                stack.append((y, x))
                visited[y][x] = True
                result += 1
            elif ele.isupper():
                if ele.lower() in keys:
                    stack.append((y, x))
                    visited[y][x] = True
                else:
                    try:
                        if (y,x) in doors[ele]:
                            return
                        doors[ele].append((y, x))
                    except:
                        doors[ele] = [(y, x)]
            elif ele.islower():
                try:
                    for next in doors[ele.upper()]:
                        stack.append(next)
                        visited[next[0]][next[1]] = True
                except:
                    pass
                finally:
                    stack.append((y, x))
                    visited[y][x] = True
                    keys.add(ele)

    for i in range(w):
        if building[0][i] != '*':
            func(building[0][i], 0, i)
        if building[h-1][i] != '*':
            func(building[h-1][i], h-1, i)
            
    for j in range(0, h):
        if building[j][0] != '*':
            func(building[j][0], j, 0)
        if building[j][w-1] != '*':
            func(building[j][w-1], j, w-1)
        

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    while stack:
        now = stack.pop()
        y = now[0]
        x = now[1]
        for i in range(4):
            if 0 <= dy[i] + y < h and 0 <= dx[i] + x < w:
                if building[dy[i] + y][dx[i] + x] != '*':
                    func(building[dy[i] + y][dx[i] + x], dy[i] + y,  dx[i] + x)
    print(result)