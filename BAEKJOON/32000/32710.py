N = int(input())
result = 0
for x in range(2, 10):
    for y in range(1, 10):
        if N == x * y:
            result = 1
print(result)