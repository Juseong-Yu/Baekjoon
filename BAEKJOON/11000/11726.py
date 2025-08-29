N = int(input())
dp = [1, 2]
if N > 2:
    for idx in range(N-2):
        new_dp = dp[idx] + dp[idx+1]
        dp.append(new_dp)

    print(dp[-1] % 10007)
elif N == 1:
    print(1)
else:
    print(2)