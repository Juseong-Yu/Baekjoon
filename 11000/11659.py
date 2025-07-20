N, M = map(int, input().split())
lst = list(map(int, input().split()))

for _ in range(M):
    i, j = map(int, input().split())
    add = lst[i-1:j]
    print(sum(add))