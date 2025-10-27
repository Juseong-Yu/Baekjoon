T = int(input())
for t in range(T):
    arr1 = input().split()
    arr2 = []
    for ele in arr1:
        arr2.append(ele[::-1])
    print(' '.join(arr2))