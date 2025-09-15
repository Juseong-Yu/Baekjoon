T = int(input())
def find(num):
        global master
        if master[num] == num:
            return master[num]
        else:
            master[num] = find(master[num])
            return master[num]
for t in range(1, T + 1):
    N, M = map(int, input().split())
    master = [i for i in range(N + 1)]
    arr = list(map(int, input().split()))
    for m in range(M):
        num1 = arr[m * 2]
        num2 = arr[m * 2 + 1]
        if num1 > num2:
            small = num2
            big = num1
        else:
            small = num1
            big = num2
        master[find(big)] = find(small)
    

    
    result = len({find(i) for i in range(1, N + 1)})
    print(f'#{t} {result}')