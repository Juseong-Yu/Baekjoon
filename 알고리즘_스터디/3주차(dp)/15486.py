# 어떤 날에 도달하였을 때, 그 날에 시작하는 상담이 끝나는 날에다가 시작하는 날짜 전 날까지 가능한 최대 합을 더해서 저장한다. 
# 만약 끝나는 날에 더 큰 금액이 있으면 안바꾼다. 그 후 시작하는 날짜에 그날까지의 최대 합을 저장한다. 
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N
result = 0

for idx, ele in enumerate(dp):
    T, P = arr[idx]
    if idx + T - 1 >= N:
        pass
    else:
        if dp[idx + T - 1] < result + P:
            dp[idx + T - 1] = result + P
    if dp[idx] > result:
        result = dp[idx]
print(result)