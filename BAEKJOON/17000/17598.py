Tiger = 0
Lion = 0

for _ in range(9):
    vote = input()
    if vote == 'Tiger':
        Tiger += 1
    elif vote == 'Lion':
        Lion += 1

if Tiger > Lion:
    print('Tiger')
elif Tiger < Lion:
    print('Lion')