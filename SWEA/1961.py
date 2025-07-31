T = int(input())

def rotate_270(box):
    new_box = []
    for x in range(N - 1, -1, -1):
        line = []
        for y in range(0, N):
            ele = box[y][x]
            line.append(ele)
        new_box.append(line)
    return new_box



for t in range(1, T + 1):
    N = int(input())
    box = []
    for _ in range(N):
        line = list(map(int, input().split()))
        box.append(line)
    r_270 = rotate_270(box)
    r_180 = rotate_270(r_270)
    r_90 = rotate_270(r_180)
    print(f'#{t}')
    for line in zip(r_90, r_180, r_270):
        for ele3 in line:
            for ele in ele3:
                print(ele, end='')
            print(' ', end='')
        print()