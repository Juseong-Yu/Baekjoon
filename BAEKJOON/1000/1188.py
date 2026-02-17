N, M = map(int, input().split())

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

while True:
    if N == M:
        print(0)
        break
    elif N > M:
        if N % M == 0:
            print(0)
            break
        else:
            N = N % M
    elif N < M:
        if M % N == 0:
            print((M // N - 1) * N)
            break
        else:
            print(M - gcd(M,N))
            break