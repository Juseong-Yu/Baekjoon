from itertools import permutations

N = int(input())
arr = [2, 3, 4, 5, 6, 7, 8, 9]
arr = list(permutations(arr, 8))
times = []
for idx in range(len(arr)):
    time = list(arr[idx][:3]) + [1] + list(arr[idx][3:])
    times.append(time)
innings = []
for _ in range(N):
    inning = list(map(int, input().split()))
    innings.append(inning)

result = 0
max_time = None
for time in times:
    score = 0
    hitter = 0
    for inning in innings:
        out = 0
        bases = [False, False, False]
        while out < 3:
            hit = time[hitter] - 1
            #print(hitter, hit)
            if inning[hit] == 1:
                if bases[2] == True:
                    score += 1
                    bases[2] = False
                if bases[1] == True:
                    bases[1] = False
                    bases[2] = True
                if bases[0] == True:
                    bases[1] = True
                    bases[0] = False
                bases[0] = True

            elif inning[hit] == 2:
                if bases[2] == True:
                    score += 1
                    bases[2] = False
                if bases[1] == True:
                    bases[1] = False
                    score += 1
                if bases[0] == True:
                    bases[2] = True
                    bases[0] = False
                bases[1] = True
            
            elif inning[hit] == 3:
                if bases[2] == True:
                    score += 1
                    bases[2] = False
                if bases[1] == True:
                    score += 1
                    bases[1] = False
                if bases[0] == True:
                    score += 1
                    bases[0] = False
                bases[2] = True

            elif inning[hit] == 4:
                if bases[2] == True:
                    score += 1
                    bases[2] = False
                if bases[1] == True:
                    score += 1
                    bases[1] = False
                if bases[0] == True:
                    score += 1
                    bases[0] = False
                score += 1

            elif inning[hit] == 0:
                out += 1
            if hitter == 8:
                hitter = 0
            else:
                hitter += 1
    if score > result:
        result = score
        max_time = time
print(result)