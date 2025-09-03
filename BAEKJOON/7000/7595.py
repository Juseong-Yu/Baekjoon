while True:
    n = int(input())
    if n == 0:
        break
    else:
        for idx in range(1, n + 1):
            print('*' * idx)