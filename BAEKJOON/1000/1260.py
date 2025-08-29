from collections import deque

N, M, V = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

for idx in range(len(edges)):
    edges[idx].sort()

visited = [False] * (N + 1)
stack = [V]
DFS = []
while stack:
    now = stack.pop()
    if visited[now] == True:
        continue
    visited[now] = True
    DFS.append(now)
    
    nexts = edges[now]
    for next in reversed(nexts):
        if visited[next] == False:
            stack.append(next)

DFS = ' '.join(list(map(str, DFS)))
print(DFS)

visited = [False] * (N + 1)
visited[V] = True
queue = deque()
queue.append(V)
BFS = []

while queue:
    now = queue.popleft()
    BFS.append(now)
    
    nexts = edges[now]
    nexts.sort()
    for next in nexts:
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
BFS = ' '.join(list(map(str, BFS)))
print(BFS)