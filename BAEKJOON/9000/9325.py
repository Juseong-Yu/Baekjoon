T = int(input())
for t in range(T):
    s = int(input())
    N = int(input())
    result = s
    for n in range(N):
        q, p = map(int, input().split())
        result += q * p
    print(result)