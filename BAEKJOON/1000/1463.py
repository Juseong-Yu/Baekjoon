N = int(input())
count = 0
dp = [N] *( N + 1)
dp[1] = 1

for idx in range(1, N+1):
    if idx * 3 < N + 1 and dp[idx] + 1 < dp[idx * 3]:
        dp[idx*3] = dp[idx] + 1

    if idx * 2 < N + 1 and dp[idx] + 1 < dp[idx * 2]:
        dp[idx*2] = dp[idx] + 1

    if idx + 1 < N + 1 and dp[idx] + 1 < dp[idx +1]:
        dp[idx+1] = dp[idx] + 1

print(dp[-1]-1)