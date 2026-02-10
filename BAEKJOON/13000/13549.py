import heapq
N, K = map(int, input().split())
heap = []
visited = [False] * 200000
heapq.heappush(heap, (0, N))
visited[N] = True

while heap:
    t, n = heapq.heappop(heap)
    if n == K:
        result = t
        break
    nexts = [n - 1, n + 1]
    if 0 < n * 2 < 200000 and visited[n * 2] == False:
        heapq.heappush(heap,(t, n * 2))
        visited[n * 2] = True

    for next in nexts:
        if 0 <= next < 200000 and visited[next] == False :
            heapq.heappush(heap, (t+1, next))
            visited[next] = True

print(result)