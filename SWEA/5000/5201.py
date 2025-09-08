T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort(reverse=True)
    trucks.sort()
    result = 0

    for container in containers:
        if trucks[-1] >= container:
            result += container
            trucks.pop()
        if not trucks:
            break

    print(f'#{t} {result}')