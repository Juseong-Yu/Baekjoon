from collections import deque
N = int(input())
arr = list(map(int, input().split()))
queue = deque(arr)
dic = {}
for ele in arr:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1

left = []
while len(dic) > 2:
    ele = queue.popleft()
    if dic[ele] == 1:
        dic.pop(ele, None)
    else:
        dic[ele] -= 1

    left.append(ele)
cnt = len(queue)

while left:
    ele = left.pop()
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
    queue.appendleft(ele)

    while len(dic) > 2:
        rightele = queue.pop()
        if dic[rightele] == 1:
            dic.pop(rightele, None)
        else:
            dic[rightele] -= 1

    if cnt < len(queue):
        cnt = len(queue)

print(cnt)    