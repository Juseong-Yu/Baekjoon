N = int(input())
for n in range(N):
    A, B = map(int, input().split())
    C = A + B
    print(f'Case #{n+1}: {C}')
