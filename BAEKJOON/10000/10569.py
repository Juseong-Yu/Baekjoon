T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    result = 2 + E - V
    print(result)