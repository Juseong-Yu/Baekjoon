from pprint import pprint
T = int(input())
for t in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp1 = [[0] * K for _ in range(K)]
    dp2 = [[0] * K for _ in range(K)]
    start, end = 0, 0
    end_flag = 0
    while end_flag < K:
        if start == end:
            dp1[start][end] = arr[start]
            dp2[start][end] = arr[start]
        else:
            min_num = float('inf')
            for idx in range(start, end):
                if idx == start and idx + 1 == end:
                    check = dp1[start][idx] + dp1[idx + 1][end]
                elif idx == start:
                    check = dp1[start][idx] + dp1[idx + 1][end] + dp2[idx + 1][end]
                elif idx + 1 == end:
                    check = dp1[start][idx] + dp2[start][idx] + dp1[idx + 1][end]
                else:
                    check = dp1[start][idx] + dp2[start][idx] + dp1[idx + 1][end] + dp2[idx + 1][end]
                
                check2 = dp2[start][idx] + dp2[idx + 1][end]
                if check < min_num:
                    min_num = check
                    min_check = check2

            dp1[start][end] = min_num
            dp2[start][end] = min_check

        # 다음 노드로 가는 부분
        start += 1
        end += 1
        if end == K:
            end = end_flag + 1
            start = 0
            end_flag += 1
            #pprint(dp)
    print(dp1[0][-1] )