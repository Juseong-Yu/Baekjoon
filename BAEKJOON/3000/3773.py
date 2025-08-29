import sys
for line in sys.stdin:
    N, S = map(int,line.split())
    print(S // (N + 1))