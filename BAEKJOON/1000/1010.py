from math import factorial as ft
tryout = int(input())
for i in range(tryout):
    numbers = input().split()
    west = int(numbers[0])
    south = int(numbers[1])
    bridge = int(ft(south)/(ft(west)*ft(south-west)))
    print(bridge)