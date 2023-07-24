import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
arr1 = sorted(arr1)
dic = {}
for k in arr1:
  if(k in dic.keys()):
    dic[k] +=1
  else:
    dic[k] = 1
result = []

for n in arr2:
  left = 0
  right = len(arr1)-1
  mid = round((left + right) / 2)
  nresult = 0
  while (left <= right):
    if (arr1[mid] == n):
      nresult = 1
      break
    elif (arr1[mid] < n):
      left = mid + 1
      mid = round((left + right) / 2)
    else:
      right = mid - 1
      mid = round((left + right) / 2)
  
  if (nresult == 1):
    j = 1
    k = 1
    
    # while (True):
    #   if (mid-j <= -1):
    #     break
    #   if(arr1[mid-j] != n):
    #     break
    #   else:
    #     j +=1

    # while (True):
    #   if (mid+k >= len(arr1)):
    #     break
    #   if(arr1[mid+k] != n):
    #     break
    #   else:
    #     k +=1
    result.append(dic[n])
  else:
    result.append(0)
result = ' '.join(str(_) for _ in result)
print(result)