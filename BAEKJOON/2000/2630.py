N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0
def paper_split(row_start, row_end, col_start, col_end):
    global blue_cnt, white_cnt
    n = row_end - row_start + 1
    
    if row_end == row_start:
        color = paper[row_start][col_start]
        return color
    
    else:
        split = n // 2
        paper1 = paper_split(row_start, row_end - split, col_start, col_end - split)
        paper2 = paper_split(row_end - split + 1, row_end, col_start, col_end - split)
        paper3 = paper_split(row_end - split + 1, row_end, col_end - split + 1, col_end)
        paper4 = paper_split(row_start, row_end - split, col_end - split + 1, col_end)

        if paper1 == paper2 == paper3 == paper4:
            return paper1

        else:
            tmp_paper = [paper1, paper2, paper3, paper4]
            for check in tmp_paper:
                if check == 1:
                    blue_cnt += 1
                elif check == 0:
                    white_cnt += 1
            return None
        
paper_split(0, N - 1, 0, N - 1)
if white_cnt == 0 and blue_cnt == 0:
    if paper[0][0] == 1:
        print(0)
        print(1)
    else:
        print(1)
        print(0)
else:
    print(white_cnt)
    print(blue_cnt)