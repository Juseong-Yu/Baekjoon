T = int(input())
for t in range(1, T + 1):
    arr1 = list(input())
    arr2 = list(input())
    arr1 = set(arr1)
    nums = []
    for ele1 in arr1:
        num = 0
        for ele2 in arr2:
            if ele1 == ele2:
                num += 1
        nums.append(num)
    result = max(nums)
    print(f'#{t} {result}')