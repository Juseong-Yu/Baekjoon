T = int(input())

def brick_break(bricks, loc):
    line = bricks[loc]
    for idx, ele in enumerate(line):
        if ele != 0 :
            x_idx = idx
            val = ele
    while True:
        for bomb in range(ele):
            
        

for t in range(1, T + 1):
    N, W, H  = map(int, input().split())
    bricks = []
    for _ in range(W):
        line = list(map(int, input().split()))
        bricks.append(line)
    print(bricks)

    bricks = list(map(list, zip(*bricks)))

    # 현재 벽돌 상태, 횟수, 구슬 위치
    BFS = []
    for loc in range(W):
        BFS.append([bricks, 1, loc])
    while BFS:
        now = BFS.pop()
        