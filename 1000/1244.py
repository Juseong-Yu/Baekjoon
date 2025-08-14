T = int(input())
switchs = list(map(int, input().split()))
student_count = int(input())
students = [list(map(int, input().split())) for _ in range(student_count)]
switchs = [0] + switchs
for student in students:
    gender = student[0]
    pick = student[1]
    if gender  == 1:
        for idx in range(pick , T + 1, pick):
            switchs[idx] = 1 - switchs[idx]
    elif gender == 2:
        M = 1
        while True:
            if pick - M < 1 or pick + M > T:
                break
            if switchs[pick - M] != switchs[pick + M]:
                break
            M += 1
        switchs[pick] = 1 - switchs[pick]
        for m in range(1, M):
            switchs[pick + m] =1 - switchs[pick + m]
            switchs[pick - m] =1 - switchs[pick - m]

for idx, switch in enumerate(switchs):
    if idx == 0:
        continue
    elif idx % 20 == 0:
        print(switch, end='\n')
    else:
        print(switch, end=' ')