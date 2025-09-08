T = int(input())
for t in range(1, T + 1):
    N = int(input())
    works = [tuple(map(int, input().split())) for _ in range(N)]
    works.sort(key=lambda x : x[1])

    now = 0
    result = 0
    for work in works:
        start = work[0]
        end = work[1]
        if start >= now:
            result += 1
            now = end

    print(f'#{t} {result}')