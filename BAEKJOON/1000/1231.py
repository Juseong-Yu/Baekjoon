def inorder(T, N):
    global perfect_tree
    if T <= N:
        inorder(T * 2 + 1, N)
        perfect_tree.append(T)
        inorder(T * 2 , N)
    else:
        return

for t in range(1, 11):
    N = int(input())
    letters = [0]
    tree = [[] for _ in range(N + 1)] 
    for _ in range(N):
        info = input().split()
        letters.append(info[1])
        if len(info) == 3:
            tree[int(info[0])].append(int(info[2]))
        elif len(info) == 4:
            tree[int(info[0])].append(int(info[2]))
            tree[int(info[0])].append(int(info[3]))

    perfect_tree = []
    result = []
    inorder(1, N)
    for ele in perfect_tree:
        result.append(letters[ele])
    result.reverse()
    result = ''.join(result)
    print(f'#{t} {result}')