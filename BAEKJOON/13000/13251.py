import math

M = int(input())
rocks_cnt = list(map(int, input().split()))
K = int(input())
rock_all = 0

result = 0
for rock in rocks_cnt:
    rock_all += rock
    if rock >= K:
        result += math.comb(rock, K)
print(result / math.comb(rock_all, K))