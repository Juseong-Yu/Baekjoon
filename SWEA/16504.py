T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_num = 0
    for idx in range(N - 1):
        num = lst[idx]
        hight = N - idx - 1
        checklst = lst[idx + 1:]
        for check in checklst:
            if check >= num:
                hight -= 1
        if max_num < hight:
            max_num = hight
    print(f'#{t}', max_num)