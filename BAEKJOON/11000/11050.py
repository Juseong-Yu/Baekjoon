import math
N,K = list(map(int,input().split()))

result = math.factorial(N)/(math.factorial(K)*math.factorial(N-K))

print(int(result))