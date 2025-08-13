T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    tree = [[] for _ in range(V + 2)]
    for start, stop in edges:
        tree[start].append(stop)
    S, G = map(int, input().split())
    stack = [S]
    visited = [0] * (V + 2)
    result = 0
    while stack:
        now = stack.pop()
        if now == G:
            result = 1
            break
        else:
            next = tree[now]
            for ele in next:
                if visited[ele] == 0:
                    visited[ele] = 1
                    stack.append(ele)

    print(f'#{t} {result}')