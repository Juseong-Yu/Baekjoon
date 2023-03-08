nums = []
result = 0
for i in range(10):
    num = int(input())
    num = num % 42
    if num not in nums:
        result+=1
    nums.append(num)
print(result)