N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(N):
    line = list(map(int, input().split()))
    room.append(line)
clean = 0
while True :
    if room[r][c] == 0:
        room[r][c] = 2
        clean += 1
    if room[r + 1][c] != 0 and room[r][c + 1] != 0 and room[r - 1][c] != 0 and room[r][c-1] != 0 :
        if d == 0:
            if room[r + 1][c] == 1:
                break
            else:
                r = r + 1
        if d == 1:
            if room[r][c-1] == 1:
                break
            else:
                c = c - 1
        if d == 2:
            if room[r - 1][c] == 1:
                break
            else:
                r = r - 1
        if d == 3:
            if room[r][c + 1] == 1:
                break
            else:
                c = c + 1
        
    else : 
        while True:
            d = ( d + 3) % 4
            if d == 0:
                if room[r -1][c] != 0:
                    continue
                else:
                    r = r - 1
                    break
            elif d == 1:
                if room[r][c+1] != 0:
                    continue
                else:
                    c = c + 1
                    break
            elif d == 2:
                if room[r + 1][c] != 0:
                    continue
                else:
                    r = r + 1
                    break
            elif d == 3:
                if room[r][c - 1] != 0:
                    continue
                else:
                    c = c - 1
                    break
print(clean)