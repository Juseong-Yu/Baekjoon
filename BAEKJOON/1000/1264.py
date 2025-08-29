line = '?'
while True:
    line = input()
    result = 0
    if line == '#':
        break
    for l in line:
        if l in 'aeiuoAEIOU':
            result+=1
    print(result)