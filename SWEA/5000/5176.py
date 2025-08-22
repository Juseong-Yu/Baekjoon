T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1

    def inorder(i):
        global cnt
        if i > N:
            return
        inorder(i * 2)
        tree[i] = cnt
        cnt += 1
        inorder(i * 2 + 1)
    inorder(1)
    print(f'#{t} {tree[1]} {tree[N // 2]}')