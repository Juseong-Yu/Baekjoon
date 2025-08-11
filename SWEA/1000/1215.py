def is_palindrome(arr):
    N = len(arr)
    for i in range(N // 2):
        if arr[i] != arr[N - i - 1]:
            return False
    else:
        return True
    

for t in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    result = 0
    for y in range(8):
        for x in range(8 - N + 1):
            end_x = x + N
            check = arr[y][x : end_x]
            
            if is_palindrome(check): 
                result += 1
    
    for x in range(8):
        for y in range(8 - N + 1):
            end_y = y + N
            check = [arr[row][x] for row in range(y, end_y)]

            if is_palindrome(check):
                result += 1  
    print(f'#{t} {result}')