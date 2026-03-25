H, W = map(int, input().split())
board = list(map(int, input().split()))

result = 0
for i in range(W):
    if i == 0 or i == W - 1:
        continue

    left_max = max(board[0 : i])
    right_max = max(board[i + 1: W])
    
    num = min(left_max, right_max) - board[i]
    if num > 0:
        result += num

print(result)