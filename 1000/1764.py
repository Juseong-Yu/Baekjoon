import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(" "))

Nlist = set()
Mlist = set()
Rlist = []
for n in range(N):
  command = input().rstrip()
  Nlist.add(command)

for m in range(M):
  command = input().rstrip()
  Mlist.add(command)

for check in Nlist:
  if check in Mlist:
    Rlist.append(check)

print(len(Rlist))
Rlist.sort()
for r in Rlist:
  print(r)