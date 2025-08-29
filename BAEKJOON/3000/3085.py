import sys
import copy
#input = sys.stdin.readline().rstrip

# 보드 입력
N = int(input())
board = []
for _ in range(N):
  line = list(input())
  board.append(line)
boardtmp = copy.deepcopy(board)

# 현재 값이 포함된 행과 열의 maxstraight 값 비교
def checkmax(board, row, col):
  countrow = 1
  maxrow = 0
  for i in range(1, N):
    if (board[i - 1][col] == board[i][col]):
      countrow += 1
      if countrow >= maxrow:
        maxrow = countrow
    else:
      countrow = 1

  countcol = 1
  maxcol = 0
  for j in range(1,N):
    if (board[row][j-1] == board[row][j]):
      countcol += 1
      if countcol >= maxcol:
        maxcol = countcol
    else:
      countcol = 1
  return max(maxrow, maxcol)

# 모든 이동을 고려하여 가장 긴 연속숫자 찾기
maxResult = 0
for row in range(N):
  for col in range(N):
    if row != N-1 and col != N-1:
      boardtmp[row][col], boardtmp[row][col + 1] = boardtmp[row][col + 1], boardtmp[row][col]
      maxResult = max(checkmax(boardtmp, row, col+1 ), checkmax(boardtmp, row, col), maxResult)
      boardtmp = copy.deepcopy(board)
      boardtmp[row][col], boardtmp[row + 1][col] = boardtmp[row + 1][col], boardtmp[row][col]
      maxResult = max(checkmax(boardtmp, row + 1, col), checkmax(boardtmp, row, col), maxResult)
      boardtmp = copy.deepcopy(board)
    elif row == N-1 and col != N-1:
      boardtmp[row][col], boardtmp[row][col + 1] = boardtmp[row][col + 1], boardtmp[row][col]
      maxResult = max(checkmax(boardtmp, row, col +1), checkmax(boardtmp, row, col), maxResult)
      boardtmp = copy.deepcopy(board)
    elif row != N-1 and col == N-1:
      boardtmp[row][col], boardtmp[row + 1][col] = boardtmp[row + 1][col], boardtmp[row][col]
      maxResult = max(checkmax(boardtmp, row + 1, col), checkmax(boardtmp, row, col), maxResult)
      boardtmp = copy.deepcopy(board)
print(maxResult)