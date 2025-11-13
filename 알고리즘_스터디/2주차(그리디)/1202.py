# 풀이 : 우선 가방과 보석을 무게를 기준으로 정렬한다. 그 다음 가방들을 돌면서 넣을 수 있는 보석을 힙에 넣은 후
# 가치가 가장 큰 보석을 꺼내에 가진다. 가방이 무게로 정렬되어있기 때문에, 현재 힙에 들어가있는 보석들은 다음 가방을 검사할 때
# 그대로 추가 가능한 보석만 넣고 다음 가방에 넣을, 가치가 가장 큰 보석을 찾아서 가진다 -> 를 반복
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