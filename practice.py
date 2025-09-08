next = [[1,2,3],[4,5,6],[7,8,9]]
real_next = [[0] * 3 for _ in range(3)]
for y in range(3):
    for x in range(3):
        real_next[2 - x][2 - y] = next[y][x]
print(real_next)

real_real_next = []
for next in real_next:
    real_real_next.append(list(reversed(next)))

print(real_real_next)