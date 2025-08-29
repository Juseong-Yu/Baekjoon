L = int(input())
N = int(input())
eat = [False] * (L + 1)
expect = []
real = []
for n in range(1, N + 1):
    P, K = map(int, input().split())
    expect.append(K - P + 1)
    count_real= 0
    for idx in range(P, K + 1):
        if eat[idx] == False:
            eat[idx] = True
            count_real += 1
    real.append(count_real)
print(expect.index(max(expect)) + 1)
print(real.index(max(real)) + 1)