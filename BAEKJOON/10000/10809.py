s = input()
list1 = [-1] * 26
for i in range(len(s)):
    if list1[(ord(s[i])-97)] == -1:
        list1[(ord(s[i])-97)] = i
for i in range(len(list1)):
    print(list1[i], end=' ')