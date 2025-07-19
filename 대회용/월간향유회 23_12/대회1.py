import sys

N, M = input().split(' ')
N = int(N)
M = int(M)
result = 0
for i in range(N):
  R = list(input())
  Y = 0
  for j in range(M):
    if R[j] == "O":
      Y += 1
  if Y >= int(M/2)+1:
    result += 1

print(result)