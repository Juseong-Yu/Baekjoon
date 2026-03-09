arr = input()
loc = [1, 0, 0, 2]
for ele in arr:
    if ele == 'A':
        loc[0], loc[1] = loc[1], loc[0]
    elif ele == 'B':
        loc[0], loc[2] = loc[2], loc[0]
    elif ele == 'C':
        loc[0], loc[3] = loc[3], loc[0]
    elif ele == 'D':
        loc[2], loc[1] = loc[1], loc[2]
    elif ele == 'E':
        loc[3], loc[1] = loc[1], loc[3]
    if ele == 'F':
        loc[2], loc[3] = loc[3], loc[2]

for idx, el in enumerate(loc):
    if el == 1:
        small = idx

    elif el == 2:
        big = idx

print(small + 1)
print(big + 1)