T = int(input())
for t in range(1, T + 1):
    profit = 0
    N = int(input())
    for i in range(N):
        line = list(map(int,list(input())))
        if i <= N // 2:
            farm = line[N // 2 - i: (N // 2) + 1 + i]
        elif i > N // 2 - 1:
            i = N - i
            farm = line[N // 2 - i + 1: (N // 2) + i]
        profit  += sum(farm)
    print(f'#{t}', profit)