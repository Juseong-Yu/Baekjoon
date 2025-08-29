N = int(input())
arr = []
ans = []
for i in range(N):
  x,y = input().split(' ')
  arr.append([int(x),int(y)])
for j in range(N):
  count = 0
  for k in range(N):
    if arr[j][0] < arr[k][0] and arr[j][1] < arr[k][1]:
      count += 1
  ans.append(count+1)
for d in ans:
  print(d,end=' ')