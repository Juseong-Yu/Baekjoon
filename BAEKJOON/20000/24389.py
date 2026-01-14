N = int(input())
arr1 = []
# 현재 수 
while N != 0:
    arr1.append(N % 2)
    N = N // 2
#print(arr1)

# 32비트로 늘리기 
while len(arr1) < 32:
    arr1.append(0)
#print(arr1)

# 보수 진행
arr2 = arr1.copy()
for idx, ele in enumerate(arr2):
    if ele == 0:
        arr2[idx] = 1
    else:
        arr2[idx] = 0
#print(arr2)

# 1 더하기
for idx, ele in enumerate(arr2):
    if idx == 0 or tmp == 1:
        ele += 1

    if ele == 2:
        tmp = 1
        ele = 0
    else:
        tmp = 0
    arr2[idx] = ele

#print(arr2)

cnt = 0
for idx in range(32):
    if arr1[idx] != arr2[idx]:
        cnt += 1

print(cnt)