count = int(input())
for i in range(count):
    score = 0
    row = 0
    result = input()
    for j in result:
        if j == 'O':
            row +=1
            score += row
        else:
            row = 0
    print(score)