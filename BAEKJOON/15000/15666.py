from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))
permu = combinations_with_replacement(arr, M)

# 안에꺼 정렬 -> set으로 중복 제거 -> 밖에 정렬
permu = list(map(sorted, permu))
permu = list(map(tuple, permu))
permu = set(permu)
permu = list(permu)
permu.sort()
for ele in permu:
    print(*ele)