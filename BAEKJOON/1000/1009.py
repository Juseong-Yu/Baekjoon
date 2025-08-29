count = int(input())
for i in range(count):
    data = list(map(int,input().split()))
    a = data[0]
    b = data[1]
    b = b % 4
    if b == 0:
        b = 4
    result = (a**b) % 10
    if result == 0:
        print(10)
    else:
        print(result)