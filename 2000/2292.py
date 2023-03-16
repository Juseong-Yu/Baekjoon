N = int(input())
dis = 1
tmp2 = 1
adder = 6

while tmp2 < N:
    tmp2 += adder
    adder += 6
    dis += 1

print(dis)
