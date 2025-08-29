N = int(input())
print('Gnomes:')
for _ in range(N):
    arr = list(map(int, input().split()))
    if arr[0] > arr[1]:
        before = 101
        for ele in arr:
            if before < ele:
                print('Unordered')
                break
            before = ele
        else:
            print('Ordered')
    else:
        before = -1
        for ele in arr:
            if before > ele:
                print('Unordered')
                break
            before = ele
        else:
            print('Ordered')