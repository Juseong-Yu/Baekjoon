T = int(input())
for t in range(1, T + 1):
    boxes = list(map(int, input().split()))
    
    before = 0
    for box in boxes:
        if box <= before:
            break
        before = box
    else:
        print(f'#{t} 0')
        continue

    before = float('inf')
    result = 0
    boxes.reverse()
    for box in boxes:
        if box < before:
            before = box
        else:
            result += box - before + 1
            before = before - 1

        if before <= 0:
            print(f'#{t} -1')
            break
    else:
        print(f'#{t} {result}')

    