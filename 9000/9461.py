N = int(input())

p = [1, 1, 1, 2, 2]
for idx in range(95):
    p.append(p[idx] + p[idx+4])

for _ in range(N):
    num = int(input())
    print(p[num-1])