T = int(input())
for t in range(1, T + 1):
    num = float(input())
    result = ""
    while len(result) <= 11:
        num = num * 2
        if num > 1:
            result += '1'
            num -= 1
        elif num < 1:
            result += '0'
        else:
            result += '1'
            break
    else:
        print(f'#{t} overflow')
        continue
    print(f'#{t} {result}')