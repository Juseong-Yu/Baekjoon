while True:
    N = int(input())
    if N == 0:
        break
    cnt = 0
    while N:
        cnt += N
        N = N - 1
    print(cnt)