M = int(input())
X = 1000000007
result = 0
for m in range(M):
    b, a = map(int, input().split())
    while True:
        if b % a == 0:
            
    # (result * b) % X = a 
    for i in range(1, 10000000007):
        num = (X * i + a) / b
        try:
            tmp = num % 3
        except:
            continue
        else:
            num = int(num)
            result += num
            break
print(result)