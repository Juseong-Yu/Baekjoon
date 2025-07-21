import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = []
all_eat = True
for _ in range(H):
    d2 = []
    for _ in range(N):
        d1 = list(map(int, input().split()))
        d2.append(d1)
        if 0 in d1:
            all_eat = False
    box.append(d2)

count = -1
next_box = []
flag = True
no_eat = False
while flag == True:
    count += 1
    flag = False
    no_eat = False
    next_box = []
    for idx_h in range(len(box)):
        next_floor = []
        floor = box[idx_h]
        for idx_n in range(len(floor)):
            next_layer = []
            layer = floor[idx_n]
            for idx_m in range(len(layer)):
                tomato = layer[idx_m]
                if tomato == 0:
                    no_eat = True
                    if idx_h > 0 :
                        if box[idx_h - 1][idx_n][idx_m] == 1:
                            flag = True
                            tomato = 1
                    if idx_h < H - 1:
                        if box[idx_h + 1][idx_n][idx_m] == 1:
                            flag = True
                            tomato = 1
                    if idx_m > 0 :
                        if box[idx_h][idx_n][idx_m - 1] == 1:
                            flag = True
                            tomato = 1
                    if idx_m < M - 1 :
                        if box[idx_h][idx_n][idx_m + 1] == 1:
                            flag = True
                            tomato = 1
                    if idx_n > 0 :
                        if box[idx_h][idx_n - 1][idx_m] == 1:
                            flag = True
                            tomato = 1
                    if idx_n < N - 1:
                        if box[idx_h][idx_n + 1][idx_m] == 1:
                            flag = True
                            tomato = 1
                next_layer.append(tomato)
            next_floor.append(next_layer)
        next_box.append(next_floor)
    box = next_box.copy()

# no_eat = False
# for floor in box:
#     for layer in floor:
#         if 0 in layer:
#             no_eat = True

if all_eat == True:
    print(0)
elif no_eat == True:
    print(-1)
else:
    print(count)