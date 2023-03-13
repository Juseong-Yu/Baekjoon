N = int(input())
flag = 0
def check(num):
    num = str(num)
    for l in range(len(num)-2):
        if num[l] == '6' and num[l+1] == '6' and num[l+2] == '6':
            return True
    return False

for i in range(666,10000000):
    ch = check(i)
    if ch == True:
        flag +=1
    else:
        continue
    if N == flag:
        print(i)
        break