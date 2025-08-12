T = int(input())
dic = {'(' : ')', '{':'}'}
for t in range(1, T + 1):
    arr = list(input())
    stack = []
    result = 1
    for ele in arr:
        if ele in ['(', '{']:
            stack.append(ele)
        elif ele in [')', '}']:
            if not stack:
                result = 0
                break
            else:
                check = stack.pop()
                if dic[check] != ele:
                    result = 0
                    break
    if stack:
        result = 0

    print(f'#{t} {result}')