T = int(input())
for t in range(1, T + 1):
    N , K = map(int, input().split())
    box = []
    for _ in range(N):
        line = list(map(int, input().split()))
        box.append(line)
    result = 0
    for x in range(N):
        count = 0
        one_counter = 0
        for y in range(N):
            if box[y][x] == 1:
                one_counter += 1
                if one_counter == K:
                    count += 1
                elif one_counter == K+1:
                    count -= 1
            elif box[y][x] == 0:
                one_counter = 0
        result  += count
    for y in range(N):
        count = 0
        one_counter = 0
        for x in range(N):
            if box[y][x] == 1:
                one_counter += 1
                if one_counter == K:
                    count += 1
                elif one_counter == K+1:
                    count -= 1
            elif box[y][x] == 0:
                one_counter = 0
        result  += count
    print(f'#{t}', result)
    