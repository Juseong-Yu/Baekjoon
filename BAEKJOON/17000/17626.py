import math
N = int(input())
dp = [0] * (N + 1)
count = 1

for i in range(1, N + 1):
    min_count = i
    for j in range(1, int(math.sqrt(i)) + 1):
        min_count = min(min_count, dp[i - j * j] + 1)
    dp[i] = min_count
print(dp[N])