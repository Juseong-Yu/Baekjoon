import sys
sys.setrecursionlimit(10000)


sudoku = [list(map(int, input().split())) for _ in range(9)]
N = 0
for y in range(9):
    for x in range(9):
        if sudoku[y][x] != 0:
            N += 1
def backtrack(sudoku, n):
    if n == 81:
        return sudoku
    flag = False
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                flag = True
                nums = find_available(sudoku, y, x)
                if nums == []:
                    return
                else:
                    for num in nums:
                        sudoku[y][x] = num
                        res = backtrack(sudoku, n + 1)
                        if res:
                            return res
                        sudoku[y][x] = 0
                break
        if flag:
            break

def find_available(sudoku, y, x):
    row_set = set([i for i in range(1, 10)])
    col_set = set([i for i in range(1, 10)])
    box_set = set([i for i in range(1, 10)])
    for row in range(9):
        num = sudoku[y][row]
        if num != 0:
            row_set.remove(num)
    
    for col in range(9):
        num = sudoku[col][x]
        if num != 0:
            col_set.remove(num)

    box_y = y // 3
    box_x = x // 3
    for row in range(3):
        for col in range(3):
            num = sudoku[col + (box_y * 3)][row + (box_x * 3)]
            if num != 0:
                box_set.remove(num)

    result = row_set & col_set & box_set
    return sorted(list(result))

final = backtrack(sudoku, N)
final_result = []
for line in final:
    line = list(map(str, line))
    line = ' '.join(line)
    print(line)
