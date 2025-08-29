T = int(input())
arr = [[1,0],[0,1]]
for j in range(2,41):
  new_stack = [arr[j-2][0] + arr[j-1][0], arr[j-2][1] + arr[j-1][1]]
  arr.append(new_stack)
for i in range(T):
  N = int(input())
  print(arr[N][0],arr[N][1])
