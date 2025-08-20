T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    pizza_out = []
    oven = [0] * N
    check_out = [0] * N
    door = 0
    idx = 0
    while True:
        if oven[door] != 0:
            oven[door] = [oven[door][0], oven[door][1] // 2]  
            if oven[door][1] == 0:
                pizza_out.append(oven[door][0])
                oven[door] = 0

        if oven[door] == 0 and idx < M:
            pizza = pizzas[idx]
            oven[door] = [idx, pizza]
            idx += 1

        elif oven == check_out:
            break
        
        door = (door + 1) % N
    result = pizza_out[-1]
    print(f'#{t} {result + 1}')
