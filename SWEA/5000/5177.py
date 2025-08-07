T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0]
    for ele in lst:
        heap.append(ele)
        idx = len(heap) - 1
        while True:
            mom = idx // 2
            if idx % 2 == 0:
                brother = idx + 1
            else:
                brother = idx - 1
            if heap[mom] > heap[idx]:
                tmp = heap[mom]
                heap[mom] = heap[idx]
                heap[idx] = tmp
                idx = mom
            else:
                break
    result = 0
    idx = (len(heap) - 1) // 2
    while True:
        if idx == 1:
            break
        result += heap[idx]
        idx = idx // 2
    result += heap[1]
    print(f'#{t}', result)