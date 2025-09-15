def union(num1, num2):
    master1 = find(num1)
    master2 = find(num2)

    if master1 < master2:
        parents[master2] = master1
    else:
        parents[master1] = master2

def find(num):
    if parents[num] == num:
        return parents[num]
    else:
        parents[num] = find(parents[num])
        return parents[num]
    
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    for _ in range(M):
        num1, num2 = map(int, input().split())
        union(num1, num2)
    
    for idx in range(1, N + 1):
        find(idx)
    print(f'#{t} {len(set(parents)) - 1}')