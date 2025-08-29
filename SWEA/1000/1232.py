def inorder(T, N):
    if T <= N:
        if tree[T] == '+':
            result = inorder(child[T][0], N) + inorder(child[T][1], N)
        elif tree[T] == '-':
            result = inorder(child[T][0], N) - inorder(child[T][1], N)
        elif tree[T] == '*':
            result = inorder(child[T][0], N) * inorder(child[T][1], N)
        elif tree[T] == '/':
            result = inorder(child[T][0], N) // inorder(child[T][1], N)
        else:
            result = tree[T]
        return result

for t in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    child = [[] for _ in range(N + 1)]

    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 4:
            idx = int(arr[0])
            cal = arr[1]
            child1 = int(arr[2])
            child2 = int(arr[3])          
            tree[idx] = cal
            child[idx].append(child1)
            child[idx].append(child2)
                    
        if len(arr) == 2:
            idx = int(arr[0])
            num = int(arr[1])
            tree[idx] = num
    result = inorder(1, N)
    print(f'#{t} {result}')
