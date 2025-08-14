for t in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []
    back_arr = []
    for ele in arr:
        if ele == '+':
            if len(stack) == 0:
                stack.append(ele)
            else:
                next_ele = stack.pop()
                stack.append(ele)
                back_arr.append(next_ele)
        else:
            back_arr.append(ele)
        
    while stack:
        next_ele = stack.pop()
        back_arr.append(next_ele)

    stack = []
    for ele in back_arr:
        if ele == '+':
            a = stack.pop()
            b = stack.pop()
            result = int(a) + int(b)
            stack.append(result)
        else:
            stack.append(ele)

    result = stack.pop()
    print(f'#{t} {result}')