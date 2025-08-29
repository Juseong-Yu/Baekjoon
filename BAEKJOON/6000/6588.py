import sys
input = sys.stdin.readline

# 에라토스테네스의 체로 소수 구하기
is_prime = [True] * 1000001
is_prime[0] = is_prime[1] = False

for i in range(2, int(1000001 ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1000001, i):
            is_prime[j] = False

# 값 구하기
flag = True
while flag:
    N = int(input().rstrip())
    if N == 0:
        flag = False
        break
    else:
        found = False
        for prime in range(2, N//2 + 1):
            if is_prime[prime] and is_prime[N - prime]:
                print(f"{N} = {prime} + {N - prime}")
                found = True
                break
        if not found:
            print("Goldbach's conjecture is wrong.")
