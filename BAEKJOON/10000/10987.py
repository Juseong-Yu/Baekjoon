string = list(input())
result = 0
for letter in string:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        result += 1

print(result)