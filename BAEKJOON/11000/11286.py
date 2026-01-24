import heapq
N = int(input())
q = []
for n in range(N):
    num = int(input())
    if num == 0:
        if q:
            num, cal = heapq.heappop(q)
            if cal == 0:
                print(-num)
            else:
                print(num)
        else:
            print(0)
    
    else:
        if num < 0:
            heapq.heappush(q, (-num, 0))
        else:
            heapq.heappush(q, (num, 1))
    
