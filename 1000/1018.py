def checkwhite(c_board):
    score = 0
    for r in range(8):
        for c in range(8):
            if (r % 2 == 0 and c % 2 == 0) or  (r % 2 != 0 and c % 2 != 0):
                if c_board[r][c] == 'B':
                    score += 1
            else :
                if  c_board[r][c] == 'W':
                    score += 1
    return score

def checkblack(c_board):
    score = 0
    for r in range(8):
        for c in range(8):
            if (r % 2 == 0 and c % 2 == 0) or  (r % 2 != 0 and c % 2 != 0):
                if c_board[r][c] == 'W':
                    score += 1
            else :
                if  c_board[r][c] == 'B':
                    score += 1
    return score    

num = input().split()
rows = int(num[0])
cols = int(num[1])
board = []
min = 64
for i in range(rows):
    row = input()
    board.append(list(row))

for c in range(cols-7):
    for r in range(rows-7):
        n_board = []
        for k in range(8):
            n_board.append(board[r+k][c:c+8])
        score1 = checkblack(n_board)
        score2 = checkwhite(n_board)
        if score1 >= score2:
            score = score2
        else:
            score = score1     
        if score < min:
            min  = score

print(min)