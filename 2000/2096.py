N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
high = arr[0]
low = arr[0]
for level in range(1, N):
    now = arr[level]
    high = [max(high[0], high[1]) + now[0], max(high[0], high[1], high[2]) + now[1], max(high[1], high[2]) + now[2]]
    low = [min(low[0], low[1]) + now[0], min(low[0], low[1], low[2]) + now[1], min(low[1], low[2]) + now[2]]
print(max(high), min(low))