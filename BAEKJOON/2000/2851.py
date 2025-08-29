eat = [0]
road = []
for _ in range(10):
    mushroom = int(input())
    road.append(mushroom)
road.append(1000)

for mushroom in road:
    eat.append(eat[-1] + mushroom)
    if eat[-1] >= 100:
        if abs(eat[-1] - 100) > abs(eat[-2] - 100):
            print(eat[-2])
            break
        else:
            print(eat[-1])
            break