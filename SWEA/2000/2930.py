T = int(input())
for t in range(1, T + 1):
    tree = [0]
    last = 0
    result = []
    N = int(input())
    for _ in range(N):
        arr = list(map(int, input().split()))
        if len(arr) == 2:
            x = arr[1]
            tree.append(x)
            last += 1
            parent = last // 2
            child = last
            while parent and tree[parent] < tree[child]:
                tree[parent], tree[child] = tree[child], tree[parent]
                child = parent
                parent = child // 2

        else:
            if len(tree) == 1:
                result.append('-1')
            else:
                pop_num = tree[1]
                result.append(str(pop_num))
                tree[1] = tree[-1]
                tree.pop()
                last -= 1
                parent = 1
                child1 = 2
                child2 = 3
                while child1 <= last:
                    if child2 > last:
                        if tree[child1] >= tree[parent]:
                            tree[child1], tree[parent] = tree[parent], tree[child1]
                            parent = child1
                            child1 = parent * 2
                            child2 = parent * 2 + 1
                        else:
                            break
                    else:
                        if tree[child1] >= tree[parent] and tree[child1] >= tree[child2]:
                            tree[child1], tree[parent] = tree[parent], tree[child1]
                            parent = child1
                            child1 = parent * 2
                            child2 = parent * 2 + 1
                        elif tree[child2] >= tree[parent] and tree[child2] >= tree[child1]:
                            tree[child2], tree[parent] = tree[parent], tree[child2]
                            parent = child2
                            child1 = parent * 2
                            child2 = parent * 2 + 1
                        else:
                            break
    result = ' '.join(result)
    print(f'#{t} {result}')