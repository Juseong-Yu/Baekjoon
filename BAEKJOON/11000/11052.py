N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N + 1)
for idx in range(N + 1):
    for num, cost in enumerate(arr):
        num = num + 1
        if idx + num <= N and dp[idx + num] < dp[idx] + cost:
            dp[idx + num] = dp[idx] + cost

print(dp[N])