T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]
    for idx in range(E):
        mother = arr[idx * 2]
        child = arr[idx * 2 + 1]
        tree[mother].append(child)
    # stack
    stack = [N]
    result = 1
    while stack:
        now = stack.pop()
        if len(tree[now]) == 0:
            continue
        else:
            result += len(tree[now])
            stack.extend(tree[now])
    print(f'#{t} {result}')

    