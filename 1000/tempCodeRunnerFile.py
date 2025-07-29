X = int(input())
sticks = [64]
while True:
    if sticks[0] == X:
        break
    while sum(sticks) > X:
        smash = sticks.pop() / 2
        if sum(sticks) + smash >= X:
            sticks.append(smash)
        else:
            sticks.extend([smash, smash])
    result = len(sticks)
    sticks = [sum(sticks)]
    if sticks[0] == X:
        break
print(result)