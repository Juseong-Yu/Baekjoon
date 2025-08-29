o_clock = list(map(int,input().split()))
hour = o_clock[0]
min = o_clock[1]
if min < 45:
    hour -= 1
    min = 60-(45-min)
else: 
    min -= 45

if hour == -1:
    hour = 23
print(hour, min)