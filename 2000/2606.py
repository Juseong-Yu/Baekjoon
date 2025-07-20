N = int(input())
node = int(input())
pc = [[] for _ in range(N+1)]
virus = [0] * (N+1)
for _ in range(node):
    A, B = map(int, input().split())
    pc[A].append(B)
    pc[B].append(A)
def check_virus(pc, virus, check):
    virus[check] = 1
    for idx in pc[check]:
        if virus[idx] == 1:
            continue
        else:
            check_virus(pc, virus, idx)
virus[1] = 1
check_virus(pc, virus, 1)
count = 0
for i in virus:
    if i == 1:
        count += 1
print(count-1)