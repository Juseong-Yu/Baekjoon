n = int(input())
result = 0
for num in range(1, n + 1):
    for x in range(1, (num + 1) // 2 + 1):
        if num % x == 0 :
            result += 1
            # print(num, x, result)
            if num // 2 == x and num // x < x:
                # print(num, x, result, 'out')
                result -= 1
print(result)
