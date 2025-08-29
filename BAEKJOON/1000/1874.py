import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []
arr = []
n_arr = []
for i in range(n):
  num = int(input())
  arr.append(num)
  n_arr.append(i+1)

for match in arr:
  while True:
    if len(stack) == 0:
      stack.append(n_arr[0])
      n_arr.pop(0)
      result.append('+')
    elif match == stack[-1]:
      stack.pop()
      result.append('-')
      break
    elif match < stack[-1]:
      print('NO')
      sys.exit()
    else:
      stack.append(n_arr[0])
      n_arr.pop(0)
      result.append('+')

for p in result:
  print(p)