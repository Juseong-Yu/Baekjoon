N = int(input())
M = int(input())
S = list(input())

before = None
flag = False
cnt = 0
result = 0
for ele in S:
    if flag == False:
        if ele == "I":
            flag = True

        cnt = 0
    
    elif flag == True:
        if before == 'O' and ele == "I":
            cnt += 1
            if cnt >= N:
                result += 1
        elif before == "I" and ele == "O":
            pass
        else:
            if ele == "I":
                flag = True
            else:
                flag = False
            cnt = 0
    before = ele

print(result)