    for num in nums:
                        tmp_sudoku = copy.deepcopy(sudoku)
                        tmp_sudoku[y][x] = num
                        return backtrack(tmp_sudoku, n + 1)
