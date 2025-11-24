# 플로이드-워셜 : 모든 노드에서 다른 모든 노드 까지의 최소 거리를 구하고(중간노드를 설정해 어디를 갔다가 가면 저장), 거리가 m 보다 작은 경우만 아이템 값을 더해
# 그 이후, 시작 값을 기준으로 얻을 수 있는 가장 큰 아이템 값을 구함
from pprint import pprint
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
dists = [[float('inf')] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dists[i][i] = 0

for _ in range(r): # 거리 저장
    node1, node2, dist = map(int, input().split())
    dists[node1][node2] = dist
    dists[node2][node1] = dist

for mid in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            dists[start][end] = min(dists[start][end], dists[start][mid] + dists[mid][end])

max_result = 0
for start in range(1, n + 1):
    tmp_result = 0
    for end in range(1, n + 1):
        if dists[start][end] <= m:
            tmp_result += items[end - 1]
    if tmp_result > max_result:
        max_result = tmp_result

print(max_result)