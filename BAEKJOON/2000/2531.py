N, d, k, c = map(int, input().split())
belt = []
for _ in range(N):
    sushi = int(input())
    belt.append(sushi)

belt = belt + belt
max = 0
for idx in range(N):
    eat = belt[idx:idx + k] + [c]
    cnt = set(eat)
    if max < len(cnt):
        max = len(cnt)

print(max)
