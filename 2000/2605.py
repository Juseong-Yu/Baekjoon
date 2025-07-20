N = int(input())
picks = list(map(int, input().split()))
line = [1]
for idx in range(1, N):
  pick = picks[idx]
  line = line[:idx - pick] + [idx + 1] + line[idx - pick:]
print(*line)