N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

def perm(idx, local_arr):
    if idx == M:
        result.add(local_arr)
        return

    for i in arr:
        perm(idx + 1, local_arr + (i,))

perm(0, ())

result = list(result)
result.sort()

for ele in result:
    print_ele = ' '.join(map(str, ele))
    print(print_ele)