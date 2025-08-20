for t in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    while True:
        arr[0] -= (cnt + 1)
        if arr[0] <= 0:
            tmp = arr.pop(0)
            arr.append(0)
            break
        else:
            tmp = arr.pop(0)
            arr.append(tmp)
        cnt = (cnt + 1) % 5
    result = list(map(str, arr))
    result = ' '.join(result)
    print(f'#{t} {result}')