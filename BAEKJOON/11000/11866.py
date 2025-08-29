N, K = list(map(int,input().split()))
table = []
result = []
pivot = 0
for i in range(N):
    table.append(i)

for j in range(N):
    if len(table) == 1:
        r = table.pop(-1)
        result.append(r) 

    elif pivot+K-1 < len(table)-1:
        r = table.pop(pivot+K-1)
        result.append(r)
        pivot = pivot + K-1

    elif pivot+K-1 == len(table)-1:
        r = table.pop(-1)
        result.append(r)
        pivot = 0

    else:
        tmp = (pivot+K-1)%len(table)
        r = table.pop(tmp)
        result.append(r)
        pivot = tmp

print('<', end='')
for k in range(N):
    if k == N-1:
        print(result[k]+1,end='')
    else:
        print(result[k]+1, end=', ')
print('>', end='')