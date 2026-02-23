from collections import deque
n = int(input())
edges = [[] for _ in range(n + 1)]
maxcosts = [[0, 0] for _ in range(n + 1)]
tmps = [[] for _ in range(n + 1)]
treeorder = []
for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    edges[child].append(parent)
    edges[child].append(cost)
    tmps[parent].append(child)

queue = deque()
queue.append(1)
while queue:
    now = queue.popleft()
    treeorder.append(now)
    nexts = tmps[now]
    for next in nexts:
        queue.append(next)

for idx in treeorder[::-1]:
    if idx == 1:
        continue
    parent, cost = edges[idx]
    checkprice = maxcosts[idx][0] + cost
    
    if checkprice >= maxcosts[parent][0]:
        maxcosts[parent][1] = maxcosts[parent][0]
        maxcosts[parent][0] = checkprice

    elif checkprice >= maxcosts[parent][1]:
        maxcosts[parent][1] = checkprice

result = 0
for ele1, ele2 in maxcosts:
    if ele1 + ele2 > result:
        result = ele1 + ele2

print(result)