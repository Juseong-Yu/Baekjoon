while True:
    line = input()
    if line == '#':
        break
    else:
        line = list(line)
        target = line[0]
        line = line[1:]
        result = 0
        for letter in line:
            if letter.lower() == target:
                result += 1

        print(target, result)