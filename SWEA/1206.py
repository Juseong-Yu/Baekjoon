for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for idx in range(2, N -2):
        check = max(buildings[idx - 2],buildings[idx - 1], buildings[idx + 1], buildings[idx + 2])
        if check < buildings[idx]:
            result += (buildings[idx] - check)
    print(f'#{t}', result)