T = int(input())

for t in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    nums = set()
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    for y in range(4):
        for x in range(4):
            def perm(idx, y, x, num):
                global nums
                if idx == 7:
                    nums.add(num)
                    return
                for i in range(4):
                    if 0 <= y + dy[i] < 4 and 0 <= x + dx[i] < 4:
                        perm(idx + 1, y + dy[i], x + dx[i] , num + str(board[y + dy[i]][ x + dx[i]]))

            perm(0, y, x, '')

    result = len(nums)
    print(f'#{t} {result}')


