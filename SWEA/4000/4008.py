T = int(input())
for t in range(1, T + 1):
    N = int(input())
    plus, minus, multi, divide = map(int, input().split()) # 1, 2, 3, 4
    nums = list(map(int, input().split()))

    operators = ['1'] * plus + ['2'] * minus + ['3'] * multi + ['4'] * divide
    visited = [False] * (N - 1)
    
    max_result = -float('inf')
    min_result = float('inf')
    def perm(idx, cnt):
        global max_result, min_result
        if idx == (N - 1):
            if cnt > max_result:
                max_result = cnt
            if cnt < min_result:
                min_result = cnt
            return
        
        before = None
        for i, operator in enumerate(operators):
            if before == operator:
                continue
            if visited[i] == False:
                before = operator
                visited[i] = True
                if operator == '1':
                    next_cnt = cnt + nums[idx + 1] 
                elif operator == '2':
                    next_cnt = cnt - nums[idx + 1] 
                elif operator == '3':
                    next_cnt = cnt * nums[idx + 1] 
                elif operator == '4':
                    if cnt < 0:
                        next_cnt = -(-(cnt) // nums[idx + 1])
                    elif cnt >= 0:
                        next_cnt = cnt // nums[idx + 1]

                if -100000000 <= next_cnt <= 100000000:
                    perm(idx + 1, next_cnt)
                visited[i] = False
    perm(0, nums[0])
    result = max_result - min_result
    print(f'#{t} {result}')