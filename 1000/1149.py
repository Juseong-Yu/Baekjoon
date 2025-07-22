N = int(input())
costs = []
for _ in range(N) : 
    cost = list(map(int, input().split()))
    costs.append(cost)

dp = [costs[0]]
for idx in range(0, N-1):
    red = min(dp[idx][1], dp[idx][2])
    green = min(dp[idx][0], dp[idx][2])
    blue = min(dp[idx][0], dp[idx][1])
    cost = [red + costs[idx + 1][0], green+ costs[idx + 1][1], blue+ costs[idx + 1][2]]
    dp.append(cost)
print(min(dp[-1]))