import heapq

N, M, K, L, P = map(int, input().split())
traps = [False] * (N + 1)
trap_lines = map(int, input().split())
for trap in trap_lines:
    traps[trap] = True


n_roads = [[] for _ in range(N + 1)]
for _ in range(M - L):
    start, end, dist = map(int, input().split())
    n_roads[start].append((end, dist))

t_roads = [[] for _ in range(N + 1)]
t_reverse = [[] for _ in range(N + 1)]
for _ in range(L):
    start, end, dist = map(int, input().split())
    t_roads[start].append((end, dist))
    t_reverse[end].append((start, dist))

S, E = map(int, input().split())
INF = float('inf')
costs = [[INF] * (N + 1) for _ in range(P)]
pq = [(0, S, 0, False)] # cost, 현재 노트, 스위치 누른 횟수, 현재 함정길 상태
result = -1
while pq:
    cost, node, p, state = heapq.heappop(pq)
    if node == E:
        result = cost
        break
    
    if traps[node] == True:
        p += 1
        if p == P:
            state = not state
            p = 0
            
    for nxt, nxt_cost in n_roads[node]:
        if costs[p][nxt] > cost + nxt_cost:
            heapq.heappush(pq, (cost + nxt_cost, nxt, p, state))

    if state == False:
        for nxt, nxt_cost in t_roads[node]:
            if costs[p][nxt] > cost + nxt_cost:
                heapq.heappush(pq, (cost + nxt_cost, nxt, p, state))
    else:
        for nxt, nxt_cost in t_reverse[node]:
            if costs[p][nxt] > cost + nxt_cost:
                heapq.heappush(pq, (cost + nxt_cost, nxt, p, state))

print(result)