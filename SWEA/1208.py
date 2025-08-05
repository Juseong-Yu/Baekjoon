for t in range (1, 11):
    dump_num = int(input())
    arr = list(map(int, input().split()))
    for dump in range(dump_num):
        max_idx = None
        min_idx = None
        max_ele = 0
        min_ele = float('inf')
        for idx, ele in enumerate(arr):
            if ele > max_ele:
                max_ele = ele
                max_idx = idx
            if ele < min_ele:
                min_ele = ele
                min_idx = idx

        arr[max_idx] -= 1
        arr[min_idx] += 1

    result = max(arr) - min(arr) 
    print(f'#{t} {result}')