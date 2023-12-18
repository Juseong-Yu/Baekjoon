import sys
input = sys.stdin.readline

K = int(input())
arr = []
result = 0
for i in range(K):
  n = int(input())
  if (n == 0):
    arr.pop()
  else:
    arr.append(n)

for num in arr:
  result += num
print(result)