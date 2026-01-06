M, N = map(int, input().split())

if M > N:
    result = N * 2 - 1
else:
    result = M * 2 - 2

print(result)