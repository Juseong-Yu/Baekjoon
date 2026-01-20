import heapq
T = int(input())
for t in range(T):
    K = int(input())
    maxQ = []
    minQ = []
    maxq = []
    minq = []
    for k in range(K):
        cal, num = input().split()
        num = int(num)
        if cal == 'I':
            heapq.heappush(maxQ, -num)
            heapq.heappush(minQ, num)
        else:
            if num == 1:
                while maxQ and maxq:
                    if -maxQ[0] == -maxq[0]:
                        heapq.heappop(maxQ)
                        heapq.heappop(maxq)
                    else:
                        break
                if maxQ:
                    tmp = -heapq.heappop(maxQ)
                    heapq.heappush(minq, tmp)

            else:
                while minQ and minq:
                    if minQ[0] == minq[0]:
                        heapq.heappop(minQ)
                        heapq.heappop(minq)
                    else:
                        break
                if minQ:
                    tmp = heapq.heappop(minQ)
                    heapq.heappush(maxq, -tmp)
        #print(maxQ, minQ, maxq, minq)

    while maxQ and maxq:
                    if -maxQ[0] == -maxq[0]:
                        heapq.heappop(maxQ)
                        heapq.heappop(maxq)
                    else:
                        break
    
    while minQ and minq:
                    if minQ[0] == minq[0]:
                        heapq.heappop(minQ)
                        heapq.heappop(minq)
                    else:
                        break
    if maxQ and minQ:
        print(-maxQ[0], minQ[0])
    else:
        print('EMPTY')
    