T = int(input())
for t in range(1, T + 1):
    N, mini, maxi = map(int, input().split())
    students = list(map(int, input().split()))
    diff = 101
    scores = [0] * 101
    for student in students:
        scores[student] += 1
    for score1 in range(1, 100):
        for score2 in range(score1, 101):
            groupA = 0
            groupB = 0
            groupC = 0
            for idx, nums in enumerate(scores):
                if idx >= score2:
                    groupA += nums
                elif idx >= score1:
                    groupB += nums
                else:
                    groupC += nums
            group_max = max(groupA,groupC,groupB)
            group_min = min(groupA,groupB,groupC)
            if group_max <= maxi and group_min >= mini:
                if diff > group_max - group_min:
                    diff = group_max - group_min
    if diff == 101:
        print(f'#{t} -1')
    else:
        print(f'#{t} {diff}')
