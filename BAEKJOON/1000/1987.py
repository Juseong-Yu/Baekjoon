R, C = map(int, input().split())
board = []
for _ in range(R):
    line = input()
    board.append(line)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
result = 0

def DFS(moved, y, x):
    global result
    if len(moved) > result:
        result = len(moved)

    for i in range(4):
        if 0 <= dy[i] + y < R and 0 <= dx[i] + x < C:
            ele = board[dy[i] + y][dx[i] + x]
            length = len(moved)
            moved.add(ele)
            if len(moved) != length:
                DFS(moved, dy[i] + y, dx[i] + x)
                moved.remove(ele)

DFS({board[0][0]}, 0, 0)

print(result)