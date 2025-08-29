N, K = map(int, input().split())
cnt = 0
for num in range(1, N + 1):
    if N % num == 0:
        cnt += 1
        if cnt == K:
            print(num)
            break
else:
    print(0)