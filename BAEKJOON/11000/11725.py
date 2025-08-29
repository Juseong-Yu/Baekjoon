import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N  +1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0] * (N + 1)
stack = [1]
while stack:
    now = stack.pop()
    sons = graph[now]
    for son in sons:
        if result[son] == 0:
            result[son] = now
            stack.append(son)
for mom in result[2:]:
    print(mom)