import sys
input = sys.stdin.readline

N = int(input())
arr = []
added = 0
for i in range(N):
  num = int(input())
  added += num
  arr.append(num)
length = len(arr)

#산술 평균
S = int(round(added/length))
print(S)

#중앙값
arr.sort()
G = arr[int(length/2)]
print(G)

#최빈값
dic = {}
for j in arr:
  if j in dic.keys():
    dic[j] = dic[j]+1
  else:
    dic[j] = 1
  
made = sorted(dic.items(), key = lambda x: x[1], reverse= True)
if len(made) == 1:
  print(made[0][0])
elif made[1][1] == made[0][1]:
  print(made[1][0])
else:
  print(made[0][0])
#범위
B = max(arr) - min(arr)
print(B)