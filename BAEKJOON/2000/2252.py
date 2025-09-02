import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
edges[0] = [i for i in range(1, N + 1)]
indegree = [1] * (N + 1)
indegree[0] = 0
for _ in range(M):
    short, tall = map(int, input().split())
    edges[short].append(tall)
    indegree[tall] += 1

order = [[0, i] for i in range(N + 1)]

cnt = 1
stack = [0]
while stack:
    next_arr = set()
    for now in stack:
        if edges[now] :
            next = edges[now]
            for ele in next:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    if order[ele][0] < cnt:
                        order[ele][0] = cnt
                        next_arr.add(ele)        
    cnt += 1
    stack = next_arr
order = order[1:]
order.sort()
result = []
for ele in order:
    result.append(str(ele[1]))
result = ' '.join(result)
print(result)