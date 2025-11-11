# - 를 만나면 다음 - 를 만날 때까지 괄호치기 -> - 뒤에 나오는 숫자는 다 음수 
lines = input()
arr = []
now = ''
for letter in lines:
    if letter == '+':
        arr.append(int(now))
        now = ''
        arr.append('+')
    elif letter == '-':
        arr.append(int(now))
        now = ''
        arr.append('-')
    else:
        now += letter
arr.append(int(now))

now = 0
flag = False
for word in arr:
    if word == '-':
        flag = True
    elif word == '+':
        pass
    else:
        if flag == True:
            now -= word
        elif flag == False:
            now += word
print(now)