from itertools import combinations
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
Combinations = combinations(arr, M)
for ele in Combinations:
    print(*ele)