T = int(input())
dp = [1, 2, 4]
for idx in range(2, 12):
    new = dp[idx-2] + dp[idx-1] + dp[idx]
    dp.append(new)
for _ in range(T):
    n = int(input())
    print(dp[n-1])