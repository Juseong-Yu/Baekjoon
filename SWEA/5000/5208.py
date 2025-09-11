T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    batterys = arr[1:]

    dp = [float('inf')] * (N + 101)
    dp[1] = 0

    for idx, battery in enumerate(batterys):
        idx += 1
        for go in range(battery + 1):
            if dp[idx + go] > dp[idx] + 1:
                dp[idx + go] = dp[idx] + 1
    result = dp[N] - 1
    print(f'#{t} {result}')