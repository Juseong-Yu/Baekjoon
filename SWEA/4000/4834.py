T = int(input())
for t in range(1, T + 1):
    counts = [0] * 10
    N = int(input())
    pick = list(map(int, list(input())))
    for ele in pick:
        counts[ele] += 1
    
    max_num = 0
    max_ele = None
    for ele, num in enumerate(counts):
        if max_num <= num:
            max_num = num
            max_ele = ele
    print(f'#{t} {max_ele} {max_num}')
