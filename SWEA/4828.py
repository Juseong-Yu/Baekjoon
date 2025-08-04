T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    max_num = max(lst)
    min_num = min(lst)
    result = max_num - min_num
    print(f'#{t}', result)