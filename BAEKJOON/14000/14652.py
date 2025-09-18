N, M, K = map(int, input().split())

cnt = 0
for y in range(N):
    for x in range(M):
        if cnt == K:
            print(y, x)
        cnt += 1