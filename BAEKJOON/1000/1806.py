N, S = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = [0] * (N + 1)
arr2[0] = 0
arr2[1] = arr1[0]
for idx in range(1, N):
    arr2[idx + 1] = arr2[idx] + arr1[idx]

result = float('inf')
i = 0
j = 1
while i != j and j < N + 1:
    check = arr2[j] - arr2[i] 
    if check >= S:
        if result > (j - i):
            result = (j - i)
        i += 1

    else:
        j += 1
if result == float('inf'):
    print(0)
else:
    print(result)