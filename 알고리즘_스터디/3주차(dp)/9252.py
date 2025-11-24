A = list(input())
B = list(input())
dp = [list([0, []]) for _ in range(len(A))  for _ in range(len(B))] # column A, row B
print(dp)
for b in range(len(B)):
    for a in range(len(A)):
        if A[a] == B[b]:
            dp[b][a][0] = 