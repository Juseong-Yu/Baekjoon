import sys
input = sys.stdin.readline

def union(a, b):
    masterA = find(a)
    masterB = find(b)
    
    if masterA == masterB:
        return
    
    if rank[masterA] < rank[masterB]:
        parents[masterA] = masterB
    elif rank[masterA] > rank[masterB]:
        parents[masterB] = masterA
    else:
        parents[masterA] = masterB
        rank[masterB] += 1

def find(num):
    if parents[num] == num:
        return parents[num]
    else:
        parents[num] = find(parents[num])
        return parents[num]

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
rank = [0] * (n + 1)
for _ in range(m):
    func, a, b = map(int, input().split())
    if func == 0:
        union(a, b)
    else:
        masterA = find(a)
        masterB = find(b)
        if masterA == masterB:
            print('YES')
        else:
            print('NO')