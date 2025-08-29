menu = []

for i in range(5):
    food = int(input())
    menu.append(food)

print(min(menu[0:3])+min(menu[3:]))