arr = list(map(int, input().split()))
add = sum(arr)
avg = add // len(arr)
result = add - avg
print(add)
print(avg)
print(result)