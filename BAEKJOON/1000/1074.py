N, r, c = map(int, input().split())
maxnum = 2 ** N - 1 
start = 1
end = 2 ** N * 2 ** N
start_r = 0
end_r = maxnum
start_c = 0
end_c = maxnum
#print(start, end, start_r, end_r, start_c, end_c)
while start_r < end_r and start_c < end_c:
    #print()
    #print(start, end, start_r, end_r, start_c, end_c)
    check_r = (start_r + end_r) // 2
    check_c = (start_c + end_c) // 2
    #print(check_r,check_c)
    start_tmp = start
    if check_r >= r and check_c >= c:
        end = start_tmp + (end - start_tmp + 1) // 4
        end_r = check_r
        end_c = check_c
        
    elif check_r >= r and check_c < c:
        start = start_tmp + (end - start_tmp + 1) // 4 
        end = start_tmp + (end - start_tmp + 1)  // 4 * 2 - 1 
        end_r = check_r
        start_c = check_c + 1

    elif check_r < r and check_c >= c:
        start_tmp = start
        start = start_tmp + (end - start + 1) // 4 * 2
        end = start_tmp + (end - start_tmp + 1) // 4 * 3 - 1
        start_r = check_r + 1
        end_c = check_c

    elif check_r < r and check_c < c:
        #print(4)
        start = start_tmp + (end - start_tmp + 1) // 4 * 3
        start_r = check_r + 1
        start_c = check_c + 1
    #print(start, end, start_r, end_r, start_c, end_c)
print(start - 1)