N = int(input())
words = input().split(' ')
for word in words[:-1]:
    print(word, end = '')
    print("DORO", end = ' ')

print(words[-1], end = '')
print("DORO", end = '')
