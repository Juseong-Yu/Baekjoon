T = int(input())
for t in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    M = max(trees)
    deficits = [M - h for h in trees]

    ones = sum(d % 2 for d in deficits)
    twos = sum(d // 2 for d in deficits)

    D = 0
    while True:
        odd_cap = (D + 1) // 2   # 홀수날 개수(= +1을 줄 수 있는 날)
        even_cap = D // 2        # 짝수날 개수(= +2를 줄 수 있는 날)
        # 짝수날이 모자라면, 부족분 하나당 홀수날 2개가 더 필요
        rem_twos = max(0, twos - even_cap)
        odd_need = ones + 2 * rem_twos
        if odd_cap >= odd_need:
            break
        D += 1

    print(f'#{t} {D}')
