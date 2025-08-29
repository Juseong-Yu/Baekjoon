N = int(input())
result = []
for start in range(1, N+1):
  check = [N, start]
  while check[-1] >= 0:
    check.append(check[-2] - check[-1])
    if len(check) > len(result):
      result = check
result = result[:-1]
print(len(result))
print(*result, sep=' ')