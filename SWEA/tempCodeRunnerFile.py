T = int(input())

def brick_break(bricks, loc):
    line = bricks[loc]
    for idx, ele in enumerate(line):
        if ele != 0 :
            x_idx = idx
            break
    bomb_continue = [[x_idx, loc]]
    while bomb_continue:
        now = bomb_continue.pop()
        x = now[0]
        y = now[1]
        val = bricks[y][x]
        for bomb in range(val):
            checks = [[x + bomb, y], [x - bomb, y], [x, y + bomb], [x , y - bomb]]
            for check in checks:
                try:
                    check_data = bricks[check[1]][check[0]]
                except:
                    continue
                else:
                    if check_data == 1:
                        bricks[check[1]][check[0]] = 0
                    elif check_data > 1:
                        bomb_continue.append([check[0], check[1]])

        bricks[y][x] = 0

    brick_break(bricks, 1)