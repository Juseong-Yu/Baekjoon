nums = input().split()
A = 0
B = 0

for i in range(len(nums[0])):
    A += int(nums[0][i])*(10**i)
for i in range(len(nums[1])):
    B += int(nums[1][i])*(10**i)
    
if A > B :
    print(A)
else:
    print(B)