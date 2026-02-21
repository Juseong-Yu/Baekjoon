N = int(input())
for _ in range(N):
    d, n, s, p = map(int, input().split())
    b = d + n * p
    j = n * s
    if b == j:
        print('does not matter')
    elif b < j:
        print('parallelize')
    elif b > j:
        print('do not parallelize')