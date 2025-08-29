T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for m in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    for idx in range(N, 0, -1):
        if tree[idx] == 0:
            if idx * 2 + 1 > N:
                tree[idx] = tree[idx * 2]
            else:
                tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
    
    print(f'#{t} {tree[L]}')