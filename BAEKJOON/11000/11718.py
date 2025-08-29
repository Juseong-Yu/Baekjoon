lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except(EOFError):
        break

for i in range(len(lines)):
    print(lines[i])