count = int(input())
list1 = []
for i in range(count):
    word = input()
    list1.append(word)
list1.sort()
list1.sort(key = len)
back =''
for i in list1:
    if back != i:
        print(i)
        back = i
    else:
        continue