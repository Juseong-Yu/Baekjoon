import sys
input = sys.stdin.readline

M,N = map(int, input().strip().split())
guide = {}
for i in range(M):
  newP = input().strip()
  guide[newP]= i+1
key = guide.keys()
key = list(key)
print(guide, key)
for j in range(N):
  Q = input().strip()
  if Q.isdecimal( ) == True:
    print(key[int(Q)-1])
  else:
    print(guide[Q])
