from collections import deque

T = int(input()) 
for t in range(1, T + 1):
    fncs = list(input())
    n = int(input())
    try:
        x = list(map(int, input().strip('[').strip(']').split(',')))
    except:
        x = []
    x = deque(x)

    result = None
    reverse = 0
    for fnc in fncs:
        if fnc == 'R':
            reverse = 1 - reverse
        elif fnc == 'D':
            if x:
                if reverse == 1:
                    x.pop()
                else:
                    x.popleft()
            else:
                result = 'error'
                break

    if result == 'error':
        print(result)
    else:
        if reverse == 1:
            x.reverse()
        x = ''.join(str(list(x)).replace(' ', ''))
        print(x)
