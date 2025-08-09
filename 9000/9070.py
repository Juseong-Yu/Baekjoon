T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cost = None
    min_cost_per_gram = float('inf')
    for gram, cost in arr:
        check = cost / gram
        if check < min_cost_per_gram:
            min_cost_per_gram = check
            min_cost = cost
        elif check == min_cost_per_gram:
            if cost < min_cost:
                min_cost = cost
                min_cost_per_gram = check

    print(min_cost)