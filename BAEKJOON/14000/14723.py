N = int(input())
a, b = 1, 1
for n in range(N - 1):
    if a == 1:
        a = b + 1
        b = 1

    else:
        a -= 1
        b += 1
print(a, b)