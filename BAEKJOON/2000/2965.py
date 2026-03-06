A, B, C = map(int, input().split())
cnt = 0
while True:
    diff_1 = B - A
    diff_2 = C - B

    if diff_1 < diff_2 and diff_2 > 1:
        A = B
        B = C - 1
        cnt += 1

    elif diff_1 >= diff_2 and diff_1 > 1:
        C = B
        B = A + 1
        cnt += 1

    else:
        break
print(cnt)