n = int(input())
num = n % 8
if 0 < num <= 5:
    print(num)
elif num == 6:
    print(4)
elif num == 7:
    print(3)
elif num == 0:
    print(2)