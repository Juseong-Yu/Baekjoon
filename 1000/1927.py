import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            result = heapq.heappop(heap)
        else:
            result = 0
        print(result)
    else:
        heapq.heappush(heap, x)
