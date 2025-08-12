T = int(input())
for t in range(1, T + 1):
    stack = []
    arr = list(input())
    for ele in arr:
        if len(stack) == 0:
            stack.append(ele)
            continue
        check = stack[-1]
        if check == ele:
            stack.pop()
        else:
            stack.append(ele)
            

    result = len(stack)
    print(f'#{t} {result}')