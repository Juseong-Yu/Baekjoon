import sys
for line in sys.stdin:
    H, P = map(int,line.split())
    num = round(H/P, 2)
    print(f'{num:.2f}')