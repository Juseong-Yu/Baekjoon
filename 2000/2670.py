N = int(input())
arr = []
for i in range(N):
  tmp = float(input())
  arr.append(tmp)
dp = [arr[0]]
for j in range(1,len(arr)):
  max1 = arr[j]
  if (dp[j-1] * arr[j] > arr[j]):
    dp.append(dp[j-1] * arr[j])
  else:
    dp.append(arr[j])
print('%0.3f' % max(dp))