from collections import deque
T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.append((A, ''))
    visited[A]  = True
    while queue:
        num, cal = queue.popleft()
        if num == B:
            break
        else:
            numD = num * 2 % 10000
            if visited[numD] == False:
                visited[numD] = True
                queue.append((numD, cal + "D"))
            
            numS = num - 1
            if numS == -1:
                numS = 9999
            if visited[numS] == False:
                visited[numS] = True
                queue.append((numS, cal + "S"))

            numL = num * 10
            if num >= 1000:
                first = num // 1000
                numL = int(str(numL)[1:]) + first
            if visited[numL] == False:
                visited[numL] = True
                queue.append((numL, cal + "L"))
            
            numR = num // 10 + (num % 10) * 1000
            if visited[numR] == False:
                visited[numR] = True
                queue.append((numR, cal + "R"))

    print(cal)