# 1, 2, ... N까지 각 수들의 약수의 합을 다시 다 더하는 문제

#생각의 전환이 필요한 문제, 각각의 약수 값이 몇번 들어가는지 갯수를 세서 더하는 방법
N = int(input())
sum = 0
for i in range(1,N+1):
  sum += (N//i) * i
print(sum)