N = int(input())
arr = list(input())
result = 0
bonus = 0
for idx, ele in enumerate(arr):
    if ele == 'O':
        result += bonus + idx + 1
        bonus += 1
    else:
        bonus = 0

print(result)