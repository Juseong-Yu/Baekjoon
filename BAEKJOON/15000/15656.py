N, M = map(int, input().split())
arr = list(map(int, input().split()))
path = []
result = set()
def perm(idx):
    if idx == M:
        result.add(tuple(path))
        return
    
    for ele in arr:
        path.append(ele)
        perm(idx + 1)
        path.pop()
perm(0)

result = list(result)
result.sort()
for ele in result:
    print(*ele)