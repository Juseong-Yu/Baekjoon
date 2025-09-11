T = int(input())
for t in range(1, T + 1):
    prices = list(map(int, input().split()))
    times = list(map(int, input().split()))
    
    visited = [False] * 12
    min_cost = prices[3]

    def find(idx, cost):
        global min_cost
        if idx >= 11:
            if min_cost > cost:
                min_cost = cost
            return cost
        
        
        
        # 1일권으로 한달
        find(idx + 1, cost + times[idx + 1] * prices[0])
        # 한달권으로 한달

        find(idx  + 1, cost + prices[1])
        
        # 세달권으로 세달
        find(idx + 3, cost + prices[2])
        return cost
    find(-1, 0)
    print(f'#{t} {min_cost}')