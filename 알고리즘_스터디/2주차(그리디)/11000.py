# 힌트 : heap에 끝나는 지점을 넣어야 한다. 다음 값이 이전 끝나는 지점 이후면 강의실 추가 x
# 풀이 : 우선 먼저 시작하는 것부터 정렬 후에 순차적으로 가면서 힙에 넣어줌, 힙에는 가장 먼저 끝나는 것을 기준으로 앞에 있음. 
# 만약 먼저 끝나는 값이 다음에 들어올 값과 시간상으로 중복되지 않으면, 먼저 끝나는 값을 빼줌
# heap에 남은 값은 가장 마지막에 넣은 값고 겹치는 모든 값임 -> 이게 최대가 되는 경우를 구하면 됨
import heapq

N = int(input())
nodes = [list(map(int, input().split())) for _ in range(N)]
nodes.sort()
heap = []
result = 0
idx = 0

while idx < N:
    if not heap or heap[0][0] > nodes[idx][0]:
        heapq.heappush(heap, (nodes[idx][1], nodes[idx][0]))
        idx += 1
    else:
        heapq.heappop(heap)
    
    if result < len(heap):
        result = len(heap)

print(result)