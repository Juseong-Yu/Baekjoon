import sys
input = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    
    else:
        parents[x] = find(parents[x])
        return parents[x]
    
def union(x, y):
    masterX = find(x)
    masterY = find(y)

    if masterX == masterY:
        return True
    
    if ranks[masterX] < ranks[masterY]:
        parents[masterX] = masterY
        return False

    elif ranks[masterY] < ranks[masterX]:
        parents[masterY] = masterX
        return False

    else:
        ranks[masterX] += 1
        parents[masterY] = masterX

n, m = map(int, input().split())
parents = [i for i in range(n)]
ranks = [0] * (n)
edges = [list(map(int, input().split())) for _ in range(m)]

cnt = 0
for s, e in edges:
    cnt += 1
    if union(s,e):
        print(cnt)
        break
else:
    print(0)