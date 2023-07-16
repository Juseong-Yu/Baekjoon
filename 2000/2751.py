import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  num = int(input())
  arr.append(num)
arr2 = sorted(arr)

for i in range(N):
  print(arr2[i])