N = int(input())
arr = list(map(int, input().split()))
result = [0] * N

for idx in range(N):
    num = idx + 1
    left_tall = arr[idx]
    for i in range(left_tall, N):
        checks = result[:i]
        zero_cnt = 0
        for check in checks:
            if check == 0:
                zero_cnt += 1

        if zero_cnt == left_tall and result[i] == 0:
            result[i] = num
            break

print(*result)