N = int(input())
cnt = 1
b = 1
while True:
    if N <= cnt:
        break
    else:
        b *= 2
        cnt = 2 ** b - 1

if b == 1:
    print(b, 'bit')
else:
    print(b, 'bits')