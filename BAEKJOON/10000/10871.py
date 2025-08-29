n = list(map(int,input().split()))
nums = list(map(int,input().split()))
N = n[0]
X = n[1]
for i in nums:
    if i < X:
        print(i, end=' ')