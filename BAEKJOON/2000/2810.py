N = int(input())
seat = list(input())
count = 0
couple = 0
for person in seat:
    if person == 'L':
        couple += 1
if couple <= 2:
    print(N)
else:
    print(int(N - (couple / 2) + 1))