N = int(input())
favors = list(map(int, input().split()))
result = 0
for favor in favors:
    if N <= favor:
        result += N
    else:
        result += favor
print(result)