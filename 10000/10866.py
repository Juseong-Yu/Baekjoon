import sys

N = int(sys.stdin.readline().strip())
D = []

for i in range(N):
  C = sys.stdin.readline().strip().split()
  if C[0] == 'push_front':
    D.insert(0,C[1])
  if C[0] == 'push_back':
    D.insert(len(D),C[1])
  if C[0] == 'pop_front':
    if(len(D) == 0):
      print(-1)
    else:
      print(D.pop(0))
  if C[0] == 'pop_back':
    if(len(D) == 0):
      print(-1)
    else:
      print(D.pop())
  if C[0] == 'size':
    print(len(D))
  if C[0] == 'empty':
    if len(D) == 0:
      print(1)
    else:
      print(0)
  if C[0] == 'front':
    if len(D) == 0:
      print(-1)
    else:
      print(D[0])
  if C[0] == 'back':
    if len(D) == 0:
      print(-1)
    else:
      print(D[-1])