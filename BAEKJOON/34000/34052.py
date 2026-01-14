check_time = 1800
for _ in range(4):
    time = int(input())
    check_time -= time

if check_time < 300:
    print('No')
else:
    print('Yes')