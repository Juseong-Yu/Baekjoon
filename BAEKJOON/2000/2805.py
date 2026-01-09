N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = 1000000000
while left < right - 1:
    cnt = 0
    h_check = (left + right) // 2
    for tree in trees:
        if tree > h_check:
            cnt += tree - h_check
    
    if cnt >= M:
        left = h_check
    
    else:
        right = h_check

print(left)