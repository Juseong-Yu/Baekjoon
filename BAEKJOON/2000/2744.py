word = input()
l = ""
for i in word:
    if i.isupper():
        l += i.lower()
    else:
        l += i.upper()

print(l)