for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    #  대각선 1
    result1 = 0
    for i in range(100):
        result1 += arr[i][i]
    
    # 대각선 2
    result2 = 0
    for j in range(100):
        result2 += arr[j][100 - 1 - j]

    # 가로
    results1 = []
    for y in range(100):
        tmp = 0
        for x in range(100):
            tmp += arr[y][x]
        results1.append(tmp)
    
    results2 = []
    for x in range(100):
        tmp = 0
        for y in range(100):
            tmp += arr[y][x]
        results2.append(tmp)
    
    result = max(result1, result2, *results1, *results2)
    print(f'#{t} {result}')
