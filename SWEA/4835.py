T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    max_num = 0
    min_num = float('inf')
    for idx in range(N - M + 1):
        nums = lst[idx: idx + M]
        num = sum(nums)
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    result = max_num - min_num

    print(f'#{t}', result)