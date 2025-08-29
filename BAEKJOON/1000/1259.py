num = ' '
while True:
    num = input()
    if num == '0':
        break
    flag = 0
    for i in range(len(num)//2):
        if num[i] != num[len(num)-1-i]:
            flag = 1
            print('no')
            break
        else:
            continue
    if flag == 0:
        print('yes')
    