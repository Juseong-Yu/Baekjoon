T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    now = 0
    result = 0
    while True:
        if now + K >= N:
            break
        for idx in range(now + K, now , -1):
            if idx in charger:
                now = idx
                result += 1
                break
        else:
            result = 0
            break
    print(f'#{t} {result}')