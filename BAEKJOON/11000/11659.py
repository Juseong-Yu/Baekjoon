N, M = map(int, input().split())
lst = list(map(int, input().split()))
stack_lst = [0]
for num in lst:
    stack_lst.append(num + stack_lst[-1])

for _ in range(M):
    i, j = map(int, input().split())
    add = stack_lst[j] - stack_lst[i-1]
    print(add)