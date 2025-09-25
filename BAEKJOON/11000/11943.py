A, B = map(int, input().split())
C, D = map(int, input().split())
tmp1 = A + D
tmp2 = C + B
print(min(tmp1, tmp2))