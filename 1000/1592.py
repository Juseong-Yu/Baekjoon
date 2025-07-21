N, M, L = map(int, input().split())
circle = [0] * N
ball = 0
count = 0
while M not in circle:
    count += 1
    circle[ball] += 1
    if circle[ball] % 2 == 1:
        ball += L
    else :
        ball -= L
    ball = ball % N
print(count - 1)