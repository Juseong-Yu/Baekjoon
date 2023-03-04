count = int(input())
for i in range(count):
    inp = input().split()
    T=int(inp[0])
    R=inp[1]
    for j in range(len(R)):
        print(R[j]*T, end='')
    print()