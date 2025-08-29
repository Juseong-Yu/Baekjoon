import sys

N = int(sys.stdin.readline().strip())
D = []
for i in range(N):
  xy = sys.stdin.readline().strip().split()
  D.append([int(xy[0]),int(xy[1])])

D.sort(key=lambda x:(x[0],x[1]))

for j in range(N):
  print(D[j][0],D[j][1])
