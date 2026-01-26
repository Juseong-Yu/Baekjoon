N = int(input())
arr1 = list(map(int, input().split()))
arr2 = []
for i in range(N):
    arr2.append([i, arr1[i], 0])

arr2.sort(key=lambda x : x[1])
cnt = 0
for idx in range(1, N):
    if arr2[idx][1] == arr2[idx - 1][1]:
        pass
    else:
        cnt += 1
    arr2[idx][2] = cnt

arr2.sort(key=lambda x : x[0])

for ele in arr2:
    print(ele[2], end=' ')