num = list(input())
if len(num) == 2:
    print(int(num[0]) + int(num[1]))
elif len(num) == 3:
    if num[1] == '0':
        print(10 + int(num[2]))
    else:
        print(int(num[0]) + 10)
else:
    print(20)