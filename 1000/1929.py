M,N = map(int,input().split())

arr = [True] * (N+1)
min_n = int(N**0.5)

for i in range(2,min_n+1):
  if arr[i] == True:
    for j in range(i+i,N+1,i):
      arr[j] = False

for i in range(N+1):
  if arr[i] == True and i >= M and i <= N and i != 1:
    print(i)