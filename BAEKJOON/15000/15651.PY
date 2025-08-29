N, M = map(int, input().split())
arr = [i for i in range(N)]

result = []
def backtrack(idx, local_arr):
    global result
    if idx == M:
        result.append(local_arr)
        return
    
    for i in range(1, N + 1):
        backtrack(idx + 1, local_arr + [i])
backtrack(0, [])

for ele in result:
    ele = list(map(str, ele))
    ele = ' '.join(ele)
    print(ele)