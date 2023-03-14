N = int(input())
flag = 0
for i in range(N):
    n = str(i)
    tmp = i
    for j in range(len(n)):
        tmp += int(n[j])
    if tmp == N:
        result = i
        flag = 1
        break

if flag == 0:
    print(0)
else:
    print(result)