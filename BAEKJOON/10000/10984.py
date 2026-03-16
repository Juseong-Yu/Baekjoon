T = int(input())
for _ in range(T):
    N = int(input())
    cnt = []
    grades = []
    for _ in range(N):
        C, G = map(float, input().split())
        cnt.append(C)
        grades.append(G)

    added_grades = 0
    added_cnt = sum(cnt)
    for idx in range(N):
        added_grades += cnt[idx] * grades[idx] 
    result_grade = added_grades / added_cnt
    print(int(added_cnt), round(result_grade, 1))