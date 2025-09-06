T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    if (a + b) != 50:
        print(50)
    else:
        print(1)