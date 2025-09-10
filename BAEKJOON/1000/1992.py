N = int(input())
video = [list(map(int, list(input()))) for _ in range(N)]

def quad_tree(row_start, row_end, col_start, col_end):
    if row_start == row_end:
        return str(video[row_start][col_start])
    
    spliter = (row_end - row_start + 1) // 2
    leaf1 = quad_tree(row_start, row_end - spliter, col_start, col_end - spliter)
    leaf2 = quad_tree(row_start, row_end - spliter, col_end - spliter + 1, col_end)
    leaf3 = quad_tree(row_end - spliter + 1, row_end, col_start, col_end - spliter)
    leaf4 = quad_tree(row_end - spliter + 1, row_end, col_end - spliter + 1, col_end)
    

    if leaf1 == leaf2 == leaf3 == leaf4 and len(leaf1) == 1 and len(leaf2) == 1 and len(leaf3) == 1 and len(leaf4) == 1:
        return str(leaf1)
    else:
        return '(' + leaf1 + leaf2 + leaf3 + leaf4 + ')'
    
result = quad_tree(0, N - 1, 0, N - 1)

print(result)