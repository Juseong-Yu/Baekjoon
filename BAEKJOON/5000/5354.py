T = int(input())
for _ in range(T):
    J = int(input())
    box = []
    for y in range(J):
        line = []
        for x in range(J):
            if y == 0 or y == J - 1 or x == 0 or x == J -1:
                line.append("#")
            else:
                line.append('J')

        liner = ''.join(line)
        box.append(liner)


    for line in box:
        print(line)
    print()