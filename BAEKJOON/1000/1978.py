N = int(input())
N_list = list(map(int,input().split()))
result = 0
for i in N_list:
    if i == 2:
        result += 1
    for k in range(2,i):
        if i % k == 0:
            break
        if k == i-1:
            result += 1

print(result)