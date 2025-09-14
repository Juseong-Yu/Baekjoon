N = input()
cnt = 0
tmp = N
while True:
    cnt += 1
    if len(tmp) == 1:
        front = '0'
        back = tmp
    else:
        front = tmp[0]
        back = tmp[1]
    next = str(int(front) + int(back))
    tmp = back + next[-1]
    if int(tmp) == int(N):
        break
print(cnt)