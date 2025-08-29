N = int(input())
scores = []
for _ in range(N):
    score = int(input())
    scores.append(score)

dp = [0] * N
dp[0] = scores[0]
if N > 1:
    dp[1] = scores[0] + scores[1]
if N > 2:
    dp[2] = max(scores[0],scores[1]) + scores[2]

for idx in range(3, N):
    dp[idx] = max(dp[idx-2] + scores[idx], dp[idx-3] + scores[idx-1] + scores[idx])

print(dp[-1])