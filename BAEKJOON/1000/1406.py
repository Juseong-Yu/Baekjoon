stack_L = list(input())
stack_R = []
T = int(input())
for t in range(T):
    com = list(input())
    if com[0] == 'P':
        stack_L.append(com[2])

    elif com[0] == 'L' and stack_L:
        stack_R.append(stack_L.pop())

    elif com[0] == 'D' and stack_R:
        stack_L.append(stack_R.pop())

    elif com[0] == 'B'and stack_L:
        stack_L.pop()

result = stack_L + stack_R[::-1]
print(''.join(result))