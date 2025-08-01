N = int(input())
switch = list(map(int, input().split()))
student_n = int(input())
students = []
for _ in range(student_n):
    student = list(map(int, input().split()))
    students.append(student)

for student in students:
    print(student)
    gender = student[0]
    num = student[1]
    if gender == 1:
        for idx in range(num - 1, student_n, num):
            if switch[idx] == 1:
                switch[idx] = 0
            else:
                switch[idx] = 1
            print(idx, num, student_n)
    else:
        idx = 0
        while True:
            print('hi')
            if num + idx < student_n and num - idx >= 0 and switch[num + idx] == switch[num - idx]:
                if idx == 0:
                    if switch[idx] == 1:
                        switch[idx] = 0
                    else:
                        switch[idx] = 1
                else:
                    if switch[num + idx] == 1:
                        switch[num + idx] = 0
                    else:
                        switch[num + idx] = 1

                    if switch[num - idx] == 1:
                        switch[num - idx] = 0
                    else:
                        switch[num - idx] = 1
            else:
                break

    print(switch)
        