line = input()
line = line.upper()
counter = dict()
for l in line:
    if l in counter.keys():
        counter[l] += 1
    else:
        counter[l] = 1
max = 0
mmax = 0
maxL = []
for key,val in counter.items():
    if max < val:
        max = val
        maxL = []
        maxL.append(key)
    elif max == val:
        maxL.append(key)

if len(maxL)>=2:
    print('?')
else:
    print(maxL[0])