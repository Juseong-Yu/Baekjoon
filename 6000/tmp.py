import sys
input = sys.stdin.readline().rstrip

# 소수 구하기
lst = [i for i in range(1,1000001)]
lst[0] = 0

for i in range(2, 1001):
  check = 2
  if lst[i-1] != 0:
    while (check * i <= 1000000):
      if lst[check * i - 1] != 0:
        lst[check * i - 1] = 0
      check += 1
filter(None, lst)
#print (lst)
#oddlst = []
#for k in range(len(lst)):
#  if lst[k] == True:
#    oddlst.append(k + 1)
oddlst = lst
# 값 구하기
flag = True
while (flag == True):
  N = int(input())
  if N == 0:
    flag = False
    break
  else:
    index = 1
    out = False
    while (oddlst[index] <= N and out == False):
      if (N - oddlst[index]) in oddlst:
        print(str(N), "=",str(oddlst[index]), "+" ,str(N - oddlst[index]))
        out = True
      index += 1
    if out == False:
      print("Goldbach's conjecture is wrong.")