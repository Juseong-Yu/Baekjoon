T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    edges = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    visited[0] = True
    for m in range(M):
        edges[arr[m * 2]].append(arr[m * 2 + 1])
        edges[arr[m * 2 + 1]].append(arr[m * 2])

    result = 0
    try:
        while True:
            i = visited.index(False)
            result += 1
            stack = [i]
            visited[i] = True
            while stack:
                now = stack.pop()
                for ele in edges[now]:
                    if visited[ele] == False:
                        visited[ele] = True
                        stack.append(ele)
    except:
        pass

    print(f'#{t} {result}')