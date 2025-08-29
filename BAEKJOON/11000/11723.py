import sys
input = sys.stdin.readline
M = int(input())
S = []

for i in range(M):
  com = input().strip().split(" ")
  if len(com) == 1:
    if com[0] == "all":
      S = list(range(1, 21))
    elif com[0] == "empty":
      S = []

  else:
    if com[0] == "add":
      if int(com[1]) not in S:
        S.append(int(com[1]))
    if com[0] == "remove":
      if int(com[1]) in S:
        S.remove(int(com[1]))
    if com[0] == "check":
      if int(com[1]) in S:
        print(1)
      else:
        print(0)
    if com[0] == "toggle":
      if int(com[1]) not in S:
        S.append(int(com[1]))
      else:
        S.remove(int(com[1]))
