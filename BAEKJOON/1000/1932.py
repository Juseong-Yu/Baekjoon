n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
before = arr[0]
for idx1 in range(1, len(arr)):
    next = []
    for idx2, ele in enumerate(arr[idx1]):
        if idx2 == 0:
            next.append(before[idx2] + ele)
        elif idx2 == len(arr[idx1]) - 1:
            next.append(before[idx2 - 1] + ele)
        else:
            next.append(max(before[idx2], before[idx2 - 1]) + ele)
    before = next
print(max(before))