total = int(input())
prices = [int(input()) for _ in range(9)]
result = total - sum(prices)
print(result)