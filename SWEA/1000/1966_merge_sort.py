T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    def merge(left, right):
        result = [0] * (len(left) + len(right))
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result[l + r] = left[l]
                l += 1
            else:
                result[l + r] = right[r]
                r += 1

        while l < len(left):
            result[l + r] = left[l]
            l += 1
        while r < len(right):
            result[l + r] = right[r]
            r += 1
        return result
    def merge_sort(li):
        if len(li) == 1:
            return li
        mid = len(li) // 2
        left = li[mid:]
        right = li[:mid]

        left_list = merge_sort(left)
        right_list = merge_sort(right)

        merge_list = merge(left_list, right_list)
        return merge_list
    
    result = merge_sort(arr)
    print(f'#{t} ', end='')
    print(*result)