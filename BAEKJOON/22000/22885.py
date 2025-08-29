T = int(input())
for t in range(1, T + 1):
    N = int(input())
    inlst = list(map(int, input().split()))
    lst = [0]
    lst.extend(inlst)
    costs = 0
    for i in range(1, N):
        ele = lst[i]
        if i == ele:
            cost = 1
            costs += cost
            j = i
        else:
            for j in range(i + 1, N + 1):
                if lst[j] == i:
                    lst = lst[:i] + list(reversed(lst[i: j + 1])) + lst[j + 1:]
                    break
            cost = j - i + 1
            costs += cost
    print(f'Case #{t}:',costs)