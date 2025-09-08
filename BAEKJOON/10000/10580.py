T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    lines.sort()
    result = 0
    for idx, line in enumerate(lines):
        for check in lines[idx + 1:]:
            if check[1] < line[1]:
                result += 1

    print(f'#{t} {result}')