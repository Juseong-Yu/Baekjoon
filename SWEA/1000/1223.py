for t in range(1, 11):
    N = int(input())
    exp = input()
    out = ''

    stack = []


    for c in exp:
        if c == '*':
            if not stack:
                stack.append(c)
            elif stack[-1] == '+':
                stack.append(c)
            else:
                while stack and stack[-1] == '*':
                    out += stack.pop()
                stack.append(c)
        
        elif c == '+':
            while stack:
                out += stack.pop()
            stack.append(c)
        
        else:
            out += c

    while stack:
        out += stack.pop()


    stack2 = []
    for c in out:
        if '0' <= c <= '9':
            stack2.append(int(c))
        elif c == '+':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1+num2)
        elif c == '*':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1*num2)

    print(f'#{t} {stack2.pop()}')