import sys
from collections import deque

N = int(sys.stdin.readline().strip())
Queue = deque()

for _ in range(N):
    C = sys.stdin.readline().strip().split()
    if C[0] == 'push':
        Queue.append(C[1])
    elif C[0] == 'pop':
        print(Queue.popleft() if Queue else -1)
    elif C[0] == 'size':
        print(len(Queue))
    elif C[0] == 'empty':
        print(0 if Queue else 1)
    elif C[0] == 'front':
        print(Queue[0] if Queue else -1)
    elif C[0] == 'back':
        print(Queue[-1] if Queue else -1)