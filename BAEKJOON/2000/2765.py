cnt = 1
pi = 3.1415927
while True:
    r, rotate, time = map(float, input().split())
    if rotate == 0:
        break
    else:
        dis = r * pi * rotate / 12 / 5280
        mph = dis / time * 60 * 60
        print(f'Trip #{cnt}: {round(dis, 2):.2f} {round(mph, 2):.2f}')
        cnt += 1
