from heapq import heappop, heappush

N = int(input())
arr = [int(input()) for _  in range(N)]
grounds = [list(map(int, input().split())) for _ in range(N)]
for idx in range(N):
    grounds[idx].append(arr[idx])

grounds.append(arr + [0])

pq = [(0, 0)] # w, node
MST = [False] * (N + 1)
min_weight = 0

while pq:
    w, n = heappop(pq)
    
    if MST[n]:
        continue

    MST[n] = 1
    min_weight += w

    for next_node in range(N + 1):
        if MST[next_node]:
            continue

        heappush(pq,(grounds[n][next_node], next_node))


print(min_weight)