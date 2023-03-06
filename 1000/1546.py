count = int(input())
score = list(map(int,input().split()))
M = max(score)
f_score = 0

for s in score:
    f_score += s/M*100
print(f_score/count)
