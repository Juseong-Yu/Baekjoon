from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
permu = permutations(arr, M)
permu = list(map(list, permu))
permu.sort()
for ele in permu:
    ele = list(ele)
    print(*ele)