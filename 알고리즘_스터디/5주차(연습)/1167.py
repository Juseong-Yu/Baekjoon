V = int(input())
nodes = [[] for _ in range(V + 1)]
for _ in range(V):
    nums = list(map(int, input().split()))
    start = nums[0]
    for idx in range(len(nums) / 2 - 1):
        end = nums[idx * 2 + 1]
        cost = nums[idx * 2 + 2]
        nodes[start].append((end, cost))

# 어떤 지점에서 끝점까지의 거리를 모두 구한다? 이거는 말도 안됨... 