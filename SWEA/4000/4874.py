T = int(input())
for t in range(1, T + 1):
    arr = list(input().split())
    stack = []
    for ele in arr:
        try:
            ele = int(ele)
            stack.append(ele)
        except:
            if ele == '.':
                result = stack.pop()
                if len(stack) != 0:
                    print(f'#{t} error')
                else:
                    print(f'#{t} {result}')
                break
            else:
                if len(stack) < 2:
                    print(f'#{t} error')
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if ele == '+':
                        num = b + a
                        stack.append(num)
                    elif ele == '-':
                        num = b - a
                        stack.append(num)
                    elif ele == '*':
                        num = b * a
                        stack.append(num)
                    elif ele == '/':
                        if a == 0:
                            print(f'#{t} error')
                            break
                        num = b / a
                        stack.append(int(num))
