import sys
input = sys.stdin.readline

TestCount = int(input())

for i in range(TestCount):
  N,M = map(int,input().split())
  arr = list(map(int,input().split()))
  count = 0
  while True:
    if arr[0] >= max(arr):
      arr.pop(0)
      count += 1
      if M == 0:
        break
      else:
        M -= 1
    else:
      tmp = arr.pop(0)
      arr.append(tmp)
      if M == 0:
        M = len(arr)-1
      else:
        M -= 1
  print(count)