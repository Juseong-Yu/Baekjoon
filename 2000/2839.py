import sys
input = sys.stdin.readline

N = int(input())
bag_3 = 0
bag_5 = -1
for i in range(N // 5 + 1):
  if (N - i * 5) % 3 == 0:
    bag_5 = i
    bag_3 = (N - i * 5) // 3

print(bag_5 + bag_3)