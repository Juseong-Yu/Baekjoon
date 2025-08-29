import sys, math
input = sys.stdin.readline

def _round(num):
  check = (num % 1) / 0.1
  if check < 5:
    return math.floor(num)
  else:
    return math.ceil(num)
  
n = int(input())
if n == 0:
  print(0)
else:
  
  p = _round(float(n * 0.15))
  arr = []
  for i in range(n):
    l = int(input())
    arr.append(l)

  added = 0

  arr.sort()

  arr = arr[p:n-p]
  for k in arr:
    added += k
  result = added / (n - (p * 2))
  print(_round(result))

# 그지같은 round...