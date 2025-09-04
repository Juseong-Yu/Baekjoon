from itertools import combinations

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
comb = combinations(arr, M)
comb = list(set(comb))
comb.sort()
for ele in comb:
    print(*ele)