call_n = int(input())
call = input().split()

Y = 0
M = 0
for i in range(call_n):
    Y_c = int(call[i])//30*10+10
    M_c = int(call[i])//60*15+15

    Y += Y_c
    M += M_c

if Y < M:
    print("Y",Y)
elif M < Y:
    print("M",M)
else:
    print("Y M",M)