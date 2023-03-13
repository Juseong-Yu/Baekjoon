N = int(input())
A = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
A = set(A)
for i in M_list:
    if i in A:
        print(1)
    else:
        print(0)