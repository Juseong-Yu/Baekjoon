list1 = []
max = 0
max_num = 0
for i in range(9):
    num = int(input())
    list1.append(num)

for i in range(9):
    if list1[i]>max:
        max = list1[i]
        max_num = i
print(max)
print(max_num+1)