N,M = list(map(int,input().split()))
first = []
second = []
result = []

for i in range(N):
    nums = list(map(int,input().split()))
    first.append(nums)

for j in range(N):
    nums = list(map(int,input().split()))
    second.append(nums)

for n in range(N):
    line = []
    for m in range(M):
        print(first[n][m]+second[n][m], end = " ")
        line.append(first[n][m]+second[n][m])
    print()
    result.append(line)
