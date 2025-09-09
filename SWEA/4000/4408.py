T = int(input())
for t in range(1, T + 1):
    N = int(input())
    corridor = [0] * (201)
    for _ in range(N):
        start, end = map(int, input().split())
        if start % 2 == 1:
            start = (start +  1) // 2
        else:
            start = start // 2
        
        if end % 2 == 1:
            end = (end + 1) // 2
        else:
            end = end // 2
    
        visits = [start, end]
        visits.sort()
        for visit in range(visits[0], visits[1] + 1):
            corridor[visit] += 1
    
    result = max(corridor)
    print(f'#{t} {result}')