import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []


for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            result = heapq.heappop(heap)
            result = - result
        else:
            result = 0
        print(result)

    else:
        heapq.heappush(heap, -num)