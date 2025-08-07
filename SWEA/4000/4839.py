def binary_search(P, find):
    time = 0
    left = 1
    right = P
    while left <= right:
        time += 1
        check = int((left+right)/2)
        if find == check:
            return time
        elif find < check:
            right = check
        else:
            left = check


T = int(input())
for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    A_time = binary_search(P, A)
    B_time = binary_search(P, B)
    if A_time > B_time:
        result = 'B'
    elif A_time < B_time:
        result = 'A'
    else :
        result = 0
    print(f'#{t} {result}')