T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        colors = list(map(int, input().split())) # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        
        y_start = colors[0]
        x_start = colors[1]
        y_go = colors[2] - colors[0]
        x_go = colors[3] - colors[1]
        color = colors[4]
        for yi in range(y_go + 1):
            for xi in range(x_go + 1): 
                if arr[y_start + yi][x_start + xi] == 0:
                    if color == 1: 
                        arr[y_start + yi][x_start + xi] = 1
                    else:
                        arr[y_start + yi][x_start + xi] = 2
                elif  arr[y_start + yi][x_start + xi] == 1:
                    if color == 2: 
                        arr[y_start + yi][x_start + xi] = 3
                elif arr[y_start + yi][x_start + xi] == 2:
                    if color == 1: 
                        arr[y_start + yi][x_start + xi] = 3

    result = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 3:
                result += 1
    print(f'#{t} {result}')