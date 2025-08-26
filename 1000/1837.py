P, K = map(int, input().split())
for check in range(2, K):
    if P % check == 0:
        print('BAD', check)
        break
else:
    print('GOOD')