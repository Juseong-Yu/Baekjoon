A, B = map(int, input().split())

cnt = 1
while True:
    if A > B:
        print(-1)
        break
    elif B % 10 == 1:
        B = (B - 1) // 10
    elif B % 2 == 0:
        B = B // 2
    else:
        print(-1)
        break
    cnt += 1
    if A == B:
        print(cnt)
        break