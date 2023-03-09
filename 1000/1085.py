x,y,w,h = list(map(int,input().split()))
d1 = w-x
d2 = h-y
d3 = x
d4 = y
print(min(d1,d2,x,y))