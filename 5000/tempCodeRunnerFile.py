n, k = map(int, input().split())
database = []
crime = []
for _ in range(n):
    finger = []
    for _ in range(5):
        line = list(input())
        finger.append(line)
    database.append(finger)

for _ in range(k):
    finger = []
    for _ in range(5):
        line = list(input())
        finger.append(line)
    crime.append(finger)
TC = 1
for finger_c in crime:
    max_same = 0
    max_same_idx = []
    for idx, finger_d in enumerate(database):
        same = 0
        for y in range(5):
            for x in range(5):
                if finger_c[y][x] == finger_d[y][x]:
                    same += 1
        if max_same < same:
            max_same = same
            max_same_idx = [idx + 1]
        elif max_same == same:
            max_same_idx.append(idx + 1)
    TC += 1
    print(f'Data Set {TC}:')
    print(*max_same_idx)
    if TC == k:
        print()