T = int(input())
for t in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    customers.sort()
    bought = 0
    for customer in customers:
        made = (customer // M) * K
        if made < bought + 1:
            print(f'#{t} Impossible')
            break
        else:
            bought += 1
    else:
        print(f'#{t} Possible')