import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, R, Q = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

stack = [R]
while stack:
    now = stack.pop()
    next = edges[now]
    for ele in next:
        edges[ele].remove(now)
    stack.extend(next)

tree_count = [0] * (N + 1)
def tree(N):
    if not edges[N]:
        tree_count[N] = 1
        return 1
    else:
        next = edges[N]
        node_cnt = 1
        for ele in next:
            if tree_count[ele] != 0:
                node_cnt = tree_count
            node_cnt += tree(ele)
        tree_count[N] = node_cnt
        return node_cnt

tree(R)

for _ in range(Q):
    U = int(input())
    print(tree_count[U])