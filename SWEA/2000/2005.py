T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [1]
    print(f'#{t}')
    print(*arr)
    for n in range(N - 1):
        next_arr = []
        for idx in range(len(arr) + 1):
            if idx == 0:
                next_arr.append(arr[idx])
            elif idx == len(arr):
                next_arr.append(arr[idx - 1])
            else:
                next_arr.append(arr[idx - 1] + arr[idx])
        print(*next_arr)
        arr = next_arr