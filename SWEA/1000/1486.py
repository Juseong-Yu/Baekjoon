T = int(input())
for t in range(1, T + 1):
    N, B = map(int,(input().split()))
    workers = list(map(int, input().split()))
    
    min_height = float('inf')
    visited = [False] * N
    
    def comb(idx, height, last):
        global min_height
        if B <= height < min_height :
            min_height = height

        if height > min_height:
            return
        
        if idx == N:
            return
        
        for i in range(last, N):
            if visited[i] == False:
                visited[i] = True
                comb(idx + 1, height + workers[i], i)
                visited[i] = False

    comb(0, 0, 0)
    result = min_height - B
    print(f'#{t} {result}')