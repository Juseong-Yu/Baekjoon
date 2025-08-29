def month(m):
    month = 0
    for M in range(m):
        if M == 2:
            month += 28
        elif M in [1,3,5,7,8,10,12]:
            month += 31
        elif M == 0:
            continue
        else:
            month += 30
    return month

start = input().split()
end = input().split()

for i in range(3):
    start[i] = int(start[i])

for i in range(3):
    end[i] = int(end[i])

if (end[0] > start[0] + 1000) or (end[0] == start[0] + 1000 and (end[1] > start[1] or (end[1] == start[1] and end[2] >= start[2]))):
    print('gg')
else:
    start_Yoon = start[0]//4 - start[0]//100 + start[0]//400
    start_d = start[0] *365 + month(start[1]) + start[2] + start_Yoon

    end_Yoon = end[0]//4 - end[0]//100 + end[0]//400
    end_d = end[0] *365 + month(end[1])+ end[2] + end_Yoon

    if ((start[0] % 4 == 0 and start[0] % 100 != 0) or  start[0] % 400 == 0) and ((start[1]==1) or (start[1] == 2 and start[2] != 29)):
        start_d -= 1

    if ((end[0] % 4 == 0 and end[0] % 100 != 0) or  end[0] % 400 == 0) and ((end[1]==1) or (end[1] == 2 and end[2] != 29)):
        end_d -= 1
    print('D-{}'.format(end_d-start_d))