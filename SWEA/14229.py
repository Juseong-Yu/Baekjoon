arr = list(map(int, input().split()))
k = 1000000
counts = [0] * (k + 1)
result = [0] * len(arr)
for ele in arr:
    counts[ele] += 1
for idx in range(len(counts) - 1):
    counts[idx + 1] += counts[idx]
for idx in range(len(arr) -1, -1, -1):
    counts[arr[idx]] -= 1
    result[counts[arr[idx]]] = arr[idx]
print(result[500000])