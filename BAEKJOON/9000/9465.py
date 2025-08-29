import sys
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    arr = list(zip(*arr))
    if n == 1:
        print(max(arr[0][0], arr[0][1]))
        continue
    dp = [[arr[0][0], arr[0][1]],[arr[0][1] + arr[1][0], arr[0][0] + arr[1][1]]]
    
    for idx in range(2, n):
        next1 = max(dp[idx - 2][0], dp[idx - 2][1], dp[idx - 1][1]) + arr[idx][0]
        next2 = max(dp[idx - 2][1], dp[idx - 2][0], dp[idx - 1][0]) + arr[idx][1]    
        dp.append([next1, next2])
    print(max(dp[-1]))