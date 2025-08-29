T = int(input())
for t in range(1, T + 1):
    dp = [0, 1, 3]
    N = int(input())
    N = N // 10
    if N >= 3:
       for idx in range(3, N + 1):
        next = dp[idx - 1] + dp[idx - 2] * 2
        dp.append(next)
    print(f'#{t} {dp[N]}') 
    