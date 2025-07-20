N, K = map(int, input().split())
girl = [0 for _ in range (6)]
boy = [0 for _ in range (6)]
count = 0
for _ in range(N):
    S , Y = map(int, input().split())
    if S == 0:
        girl[Y-1] += 1
    else : 
        boy[Y-1] += 1

for num in girl:
    if num % K != 0:
        count += num // K + 1
    else:
        count += num // K

for num in boy:
    if num % K != 0:
        count += num // K + 1
    else:
        count += num // K
print(count)