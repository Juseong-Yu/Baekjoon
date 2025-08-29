while True:
    line = list(map(int, input().split()))
    if line == [0]:
        break
    else:
        result = 1
        for idx in range(1, line[0] * 2 + 1):
            if idx % 2 == 0:
                result -= line[idx]
            else:
                result *= line[idx]
        print(result)