n = int(input())
list1 = []
list2 = []
list3 = []
flag = 1
for i in range(n):
    num = int(input())
    list1.append(num)

for i in range(1,list1[0]+1):
        list2.append(i)
        s = list1[0]+1

for l in list1[1:]:
    if list2[-1] >= l:
        if list2[-1] == l:
            list2.pop(-1)
            list3.append('-')
        else:
            flag = 0
            break

    elif list2[-1] < l:
        for i in range(s,l+1):
            list2.append(i)
            list3.append('+')
        s = l

if flag == 0:
    print('NO')
else:
    for i in list3:
        print(i)