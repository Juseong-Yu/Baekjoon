import math
string = list(input())
N = len(string)
for R in range(1, int(math.sqrt(N)) + 1):
    if N % R == 0:
        C = N / R
R = N / C
lst = [[]]
for letter in string:
    if len(lst[-1]) < R:
        lst[-1].append(letter)
    else:
        lst.append([letter])
        
for x in range(int(R)):
    for y in range(int(C)):
        print(lst[y][x], end='')
