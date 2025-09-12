N = int(input())
fluids = list(map(int, input().split()))
fluids.sort()

min_result = float('inf')
result = []

for i in range(1, N - 1):
    L = 0
    R = N - 1
    while L < i < R:
        check = sum([fluids[L], fluids[i], fluids[R]])
        if abs(check) < abs(min_result):
            min_result = check
            result = [fluids[L], fluids[i], fluids[R]]
        if check == 0:
            break
        elif check < 0:
            L += 1
        else:
            R -= 1

print(*result)