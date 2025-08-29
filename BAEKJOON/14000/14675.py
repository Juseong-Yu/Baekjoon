import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

q = int(input())
for _ in range(q):
    t, k  = map(int, input().split())
    if t == 2:
        print('yes')
    else:
        if len(tree[k]) == 1:
            print('no')
        else:
            print('yes')