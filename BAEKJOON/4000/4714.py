while True:
    num = float(input())
    if num == -1.0:
        break
    else:
        result = num * 0.167
        print(f'Objects weighing {num:.2f} on Earth will weigh {result:.2f} on the moon.')