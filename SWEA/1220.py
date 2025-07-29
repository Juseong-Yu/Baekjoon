for t in range(1, 11):
    length = int(input())
    table = []
    for _ in range(length):
        line = list(map(int,(input().split())))
        table.append(line)
    result = 0
    # 1이 빨간색 2가 파란색
    for x in range(length):
        NS = []
        count = 0
        for y in range(length):
            check = table[y][x]
            if check == 0:
                continue
            elif len(NS) == 0 and check == 2:
                continue
            elif check == 1:
                NS.append(1)
            elif NS[-1] == 1 and check == 2:
                NS.append(2)
                count += 1
            elif NS[-1] == 2 and check == 2:
                NS.append(2)
        result += count
    print(f'#{t} {result}')