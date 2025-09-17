T = int(input())
for t in range(1, T + 1):
    N = int(input())
    fields = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []

    for y in range(N):
        for x in range(N):
            if fields[y][x] == 'X':
                startX, startY = x, y
            if fields[y][x] == 'Y':
                endX, endY = x, y

    # 0 up 1 right 2 down 3 left   
    for _ in range(Q):
        num, commands = map(str, input().split())
        commands = list(commands)
        nowX = startX
        nowY = startY
        position = 0
        for command in commands:
            if command == 'A':
                if position == 0:
                    nextY = nowY - 1
                    nextX = nowX
                elif position == 1:
                    nextX = nowX + 1
                    nextY = nowY
                elif position == 2:
                    nextY = nowY + 1
                    nextX = nowX 
                elif position == 3:
                    nextX = nowX - 1
                    nextY = nowY

                if 0 <= nextX < N and 0 <= nextY < N and fields[nextY][nextX] != 'T':
                    nowX = nextX
                    nowY = nextY

            elif command == 'L':
                position -= 1
                if position == -1:
                    position = 3
            
            elif command == 'R':
                position += 1
                if position == 4:
                    position = 0

        if nowX == endX and nowY == endY:
            result.append('1')
        else:
            result.append('0')
    
    result = ' '.join(result)
    print(f'#{t} {result}')