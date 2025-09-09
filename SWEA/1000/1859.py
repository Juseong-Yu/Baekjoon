T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    max_cost = 0
    result = 0
    for ele in arr:
        if ele > max_cost:
            max_cost = ele
        else:
            result += max_cost - ele

    print(f'#{t} {result}')