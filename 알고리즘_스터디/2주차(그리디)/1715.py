# 가장 작은 2개의 묶음을 계속해서 합친다. 
from collections import deque
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
queue1 = deque(arr)
queue2 = deque()
result = 0
while len(queue1) + len(queue2) != 1:
    # queue2에서 다 뽑는 경우
    if (not len(queue1)) or (len(queue2) >= 2 and (queue1[0] > queue2[1])):
        min1 = queue2.popleft()
        min2 = queue2.popleft()
        result += min1 + min2
        queue2.append(min1 + min2)
    
    # queue1에서 다 뽑는 경우
    elif (not len(queue2)) or (len(queue1) >= 2 and (queue2[0] > queue1[1])):
        min1 = queue1.popleft()
        min2 = queue1.popleft()
        result += min1 + min2
        queue2.append(min1 + min2)
    
    # 하나씩 뽑는 경우
    else:
        min1 = queue1.popleft()
        min2 = queue2.popleft()
        result += min1 + min2
        queue2.append(min1 + min2)

print(result)