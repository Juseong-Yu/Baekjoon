import sys
for i in range(3):
  num = int(input())
  added = 0
  for j in range(num):
    add = int(sys.stdin.readline())
    added += add
  if added > 0:
    print('+')
  elif added < 0 :
    print('-')
  else :
    print('0')