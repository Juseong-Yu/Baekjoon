attendence = []

for i in range(28):
    number = int(input())
    attendence.append(number)

for j in range(1,31):
    if j not in attendence:
        print(j)