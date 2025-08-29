X = 10 ** 9 + 7
def mod_inverse(b, X):
    return pow(b, X - 2, X)

M = int(input())
result = 0

for _ in range(M):
    N, S = map(int, input().split())
    inv_N = mod_inverse(N, X)
    result = (result + S * inv_N) % X

print(result)