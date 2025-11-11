N = int(input())
P = list(map(int, input().split()))
P.sort()
count = 0
result = 0
for i in P:
    count += i
    result += count
print(result)