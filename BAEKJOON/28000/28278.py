import sys
input = lambda: sys.stdin.readline

N = int(input())
stack = []
for n in range(N):
    order = str(input())
    if order == '2':
        if stack:
            result = stack.pop()
            print(result)
        else:
            print(-1)

    elif order == '3':
        result = len(stack)
        print(result)

    elif order == '4':
        if stack:
            print(0)
        else:
            print(1)
    
    elif order == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    
    else:
        order, num = order.split()
        stack.append(int(num))

