def gababo(arr, i, j):
    if i == j:
        return i
    elif i + 1 == j:
        if arr[i] + 1 == arr[j] or arr[i] - 2 == arr[j]:
            return j
        elif arr[j] + 1 == arr[i] or arr[j] - 2 == arr[i]:
            return i
        else:
            return i
    else:
        a = gababo(arr, i, (i + j) // 2)
        b = gababo(arr,(i + j) // 2 + 1, j)
        if arr[a] + 1 == arr[b] or arr[a] - 2 == arr[b]:
            return b
        elif arr[b] + 1 == arr[a] or arr[b] - 2 == arr[a]:
            return a
        else:
            return a

        

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = gababo(arr, 0, N - 1)
    print(f'#{t} {result + 1}')