while True:
    num = list(map(int,input().split()))
    A = num[0]
    B = num[1]

    if A == 0 and B == 0:
        break

    print(A+B)