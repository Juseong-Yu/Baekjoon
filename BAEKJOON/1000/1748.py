N =int(input())
Nlength = len(str(N))
result = 0
while(Nlength > 0):
  result += (N - 10**(Nlength-1)+1) * Nlength
  N = (10**(Nlength-1))-1
  Nlength -=1


print(result)