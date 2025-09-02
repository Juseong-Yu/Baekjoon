C, N = map(int, input().split())
arr = []
for _ in range(N):
    cost, customer = map(int, input().split())
    per = cost / customer
    arr.append([per, cost, customer])

arr.sort()
dp = [float('inf')] * (C + 101)
dp[0] = 0
for num in range(C + 1):
    for ele in arr:
        per, cost, customer = ele[0], ele[1], ele[2]
        if dp[num + customer] > dp[num] + cost:
            dp[num + customer] = dp[num] + cost
find = dp[C : ]
print(min(find))