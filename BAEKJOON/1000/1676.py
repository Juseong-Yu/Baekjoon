import math
N = int(input())

fact = math.factorial(N)
count = 0
length = len(str(fact))
for i in range(length):
  if(str(fact)[length-i-1] != '0'):
    break
  else:
    count += 1

print(count)