T = int(input())
for t in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                break
        else:
            result = 1
            break
    print(f'#{t} {result}')
