T = int(input())
for t in range(1, T + 1):
    sudoku = []
    for _ in range(9):
        line = list(map(int, input().split()))