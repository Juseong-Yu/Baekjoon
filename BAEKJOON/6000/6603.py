while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    else:
        k = arr[0]
        arr = arr[1:]
    visited = [False] * k
    result = []

    def perm(idx, local_arr):
        for check_idx, check in enumerate(local_arr):
            if check_idx > 0 and check < local_arr[check_idx - 1]:
                return
        if idx == 6:
            result.append(local_arr)
        
        for i in range(k):
            if visited[i] == False:
                visited[i] = True
                perm(idx + 1, local_arr + [arr[i]])
                visited[i] = False

    perm(0, [])
    for ele in result:
        result_ele = list(map(str, ele))
        result_ele = ' '.join(result_ele)
        print(result_ele)
    print()