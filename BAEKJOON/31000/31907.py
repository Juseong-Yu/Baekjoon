K = int(input())
arr = [['G', '.', '.', '.'], ['.', 'I', '.', 'T'], ['.', '.', 'S', '.']]
for y in range(3):
    for y1 in range(K):
        for x in range(4):
            for x1 in range(K):
                print(arr[y][x], end='')
        print()
