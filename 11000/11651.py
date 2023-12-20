import sys 
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
  x,y = input().split(' ')
  arr.append([int(x),int(y)])

arr.sort(key = lambda x: (x[1],x[0]))
for j in range(N):
  print(arr[j][0], arr[j][1], end='\n', sep=' ')