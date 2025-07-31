T = int(input())
for t in range(1, T + 1):
    sudoku = []
    result = 1
    for _ in range(9):
        line = list(map(int, input().split()))
        sudoku.append(line)
    
    # 가로 확인
    for line in sudoku:
        set1 = set(line)
        if len(set1) != 9:
            result = 0
    
    # 세로 확인
    for x in range(9):
        set2 = set()
        for y in range(9):
            set2.add(sudoku[y][x])

        if len(set2) != 9:
            result = 0

    # 박스 확인
    for big_x in range(0, 3):
        for big_y in range(0, 3):
            set3 =  set()
            for x in range(0, 3):
                for y in range(0, 3):
                    real_x = big_x * 3 + x
                    real_y = big_y * 3 + y
                    set3.add(sudoku[real_y][real_x])
            if len(set3) != 9:
                result = 0