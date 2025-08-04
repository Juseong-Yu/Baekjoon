T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    costs = 0
    for idx in range(N - 1):
        ele = lst[idx]
        i = idx + 1
        if i == ele:
            cost = 1
            costs += cost
            j = i
        else:
            for j in range(idx + 1, N):
                if lst[j] == i:
                    if j == N - 1:
                        lst = lst[:idx] + list(reversed(lst[idx:]))
                    elif i == 1:
                        lst = list(reversed(lst[idx: j])) + lst[j:]

                    else:
                        lst = lst[:idx] + list(reversed(lst[idx: j])) + lst[j:]

            cost = j - idx + 1
            costs += cost
    print(f'Case #{t}:',costs)