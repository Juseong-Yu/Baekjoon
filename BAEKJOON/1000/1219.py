for _ in range(1, 11):
    t, edge_cnt = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = [[] for _ in range(100)]
    for idx in range(len(arr) // 2):
        start = arr[idx * 2]
        stop = arr[idx * 2 + 1]
        edges[start].append(stop)

    stack = [0]
    visited = [False] * 100 
    result = 0
    while stack:
        now = stack.pop()
        if now == 99:
            result = 1
            break
        else:
            next = edges[now]
            for ele in next:
                if visited[ele] == 0:
                    visited[ele] = 1
                    stack.append(ele)
    print(f'#{t} {result}')