T = int(input())
A = [i for i in range(1, 13)]
for t in range(1, T + 1):
    N, K = map(int, input().split())
    counts = 1<<12
    result = 0
    for i in range(counts):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N and sum(subset) == K:
            result += 1
    print(f'#{t} {result}')