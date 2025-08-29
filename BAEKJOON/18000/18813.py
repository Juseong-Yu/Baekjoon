n, m = map(int, input().split())
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc = list(abc)
abc = abc[:m]
words = []
for _ in range(n):
    word = input()
    words.append(word)

count = 0
for word in words:
    check_word = set(word)
    if len(check_word) == len(word):
        for letter in word:
            if letter not in abc:
                break
        else:
            count += 1

print(count)