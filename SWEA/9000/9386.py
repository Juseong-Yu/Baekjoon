T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, list(input())))
    max_cnt = 0
    cnt = 0
    for ele in arr:
        if ele == 1:
            cnt += 1
        elif ele == 0:
            if max_cnt < cnt :
                max_cnt = cnt
            cnt = 0
    if max_cnt < cnt:
        max_cnt = cnt
    print(f'#{t} {max_cnt}')
        