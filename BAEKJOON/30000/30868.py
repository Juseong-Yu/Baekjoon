T = int(input())
for t in range(T):
    num = int(input())
    fives = num // 5
    ones = num % 5
    for five in range(fives):
        print('++++', end=' ')
    for one in range(ones):
        print('|', end='')
    print()