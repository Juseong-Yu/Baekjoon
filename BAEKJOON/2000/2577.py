nums = []
for i in range(3):
    num = int(input())
    nums.append(num)
ABC = nums[0]*nums[1]*nums[2]
list1 = [0]*10
for i in str(ABC):
    list1[int(i)] += 1
for k in list1:
    print(k)