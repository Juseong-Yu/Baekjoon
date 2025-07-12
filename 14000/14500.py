import sys
#input = sys.stdin.readline().rstrip

# 입력
N, M = map(int, input().split(" "))
paper = []
for _ in range(N):
  line = list(map(int, input().split(" ")))
  paper.append(line)

def checker(arow, acol, brow, bcol, crow, ccol, drow, dcol):
  Max = 0
  for row in range(N):
    for col in range(M):
      if row + arow >= N or row + brow >= N or row + crow >= N or row + drow >= N or col + acol >= M or col + bcol >= M or col + ccol >= M or col + dcol >= M:
        continue
      else:
        check = paper[row + arow][col + acol] + paper[row + brow][col + bcol] + paper[row + crow][col + ccol] + paper[row + drow][col + dcol]
        if check >= Max:
          Max = check
  return Max

# skyblue
maxSkyblue = max(checker(0,0,0,1,0,2,0,3), checker(0,0,1,0,2,0,3,0))

# yellow
maxYellow = checker(0,0,1,0,1,1,0,1)

# orange
maxOrange = max(checker(0,0,1,0,2,0,2,1),checker(1,0,1,1,1,2,0,2), checker(0,0,0,1,1,1,2,1), checker(0,0,0,1,1,0,2,0), checker(0,0,0,1,0,2,1,0), checker(0,1,1,1,2,0,2,1), checker(0,0,0,1,0,2,1,2), checker(0,0,1,0,1,1,1,2))

# green
maxGreen = max(checker(0,0,1,0,1,1,2,1), checker(0,1,0,2,1,0,1,1), checker(0,1,1,1,1,0,2,0), checker(0,0,0,1,1,1,1,2))

# purple
maxPurple = max(checker(0,1,1,0,1,1,1,2), checker(0,0,1,0,1,1,2,0), checker(0,0,0,1,0,2,1,1), checker(0,1,1,1,1,0,2,1))

print(max(maxSkyblue, maxYellow, maxOrange, maxGreen, maxPurple))