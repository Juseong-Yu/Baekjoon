a, b = list(map(int,input().split()))
s2 = (a - b) / 2
s1 = s2 + b
flag = (a - b) % 2
if s1 >= 0 and s2 >= 0 and flag == 0:
    print(int(s1),int(s2))
else:
    print(-1)