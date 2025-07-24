word = list(input())
count = 0
for idx, letter in enumerate(word):
    if idx - 1 >= 0:
        if letter == '=':
            if word[idx - 1] == 'c' or word[idx - 1] == 's':
                count += 1
            elif word[idx - 1] == 'z':
                if idx -2 >= 0:
                    if word[idx - 2] == 'd':
                        count += 2
                    else:
                        count += 1
                else:
                    count += 1

        elif letter == '-' :
            if word[idx - 1] == 'c' or word[idx-1] == 'd':
                count += 1

        elif letter == 'j':
            if word[idx - 1] == 'l' or word[idx - 1] == 'n':
                count += 1

print(len(word) - count)
        