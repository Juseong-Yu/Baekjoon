import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
diamonds = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
diamonds.sort()
bags.sort()
heap = []
result = 0
idx = 0
for bag in bags:
    while True:
        if idx >= N :
            break
        if diamonds[idx][0] > bag:
            break
        else:
            heapq.heappush(heap, -diamonds[idx][1])
        idx += 1
    if heap:
        max_diamond = heapq.heappop(heap)
        result += -max_diamond
    else:
        continue
print(result)