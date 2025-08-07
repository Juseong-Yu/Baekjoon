T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N - 1):
        min_max_idx = i
        for j in range(i + 1, N):
            if i % 2 == 0:
                if arr[j] > arr[min_max_idx]:
                    min_max_idx = j
            if i % 2 == 1:
                if arr[j] < arr[min_max_idx]:
                    min_max_idx = j
        arr[i], arr[min_max_idx] = arr[min_max_idx], arr[i]
    arr = arr[:10]
    result = ' '.join(map(str, arr))
    print(f'#{t} {result}')