T = int(input())
for t in range(1, T + 1):
    A, B = map(list,input().split())

    len_A = len(A)
    len_B = len(B)
    idx = 0
    result = 0
    while idx != len_A :
        if A[idx: idx + len_B] == B:
            idx += len_B
        else:
            idx += 1
        result += 1

    print(f'#{t} {result}')