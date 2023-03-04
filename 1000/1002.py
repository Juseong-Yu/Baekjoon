import math
count = int(input())
for i in range(count):
    x1,y1,r1,x2,y2,r2 = list(map(int,input().split()))
    dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if dis == 0 and r1==r2:
        print(-1)
    elif dis == r1+r2 or dis == max(r1,r2)-min(r1,r2):
        print(1)
    elif dis < max(r1,r2)-min(r1,r2) or dis >r1+r2:
        print(0)
    else:
        print(2)