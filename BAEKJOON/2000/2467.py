N = int(input())
arr = list(map(int, input().split()))

start = 0
end = len(arr) - 1

min_result = float('inf')
result = None
while start != end:
    num = arr[start] + arr[end]
    if min_result >= abs(num):
        min_result = abs(num)
        result = [arr[start] , arr[end]]
    
    if num > 0:
        end -= 1
    else:
        start += 1

print(result[0], result[1])