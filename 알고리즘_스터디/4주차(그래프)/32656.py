N = int(input())
nodes = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)

a, b, x = map(int, input().split())
visited = [False] *(N + 1)
if a == x:
    a = 0
if b == x:
    b = 0

for num in [a, b]:
    stack = [num]
    while stack:
        now = stack.pop()
        visited[now] = True
        for node in nodes[now]:
            if node != x and visited[node] == False:
                stack.append(node)

result = 0
for check in visited[1:]:
    if check == False:
        result += 1
print(result)