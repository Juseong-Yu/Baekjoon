N = int(input())
timetable = []
for _ in range(N):
    start, end = map(int, input().split())
    timetable.append([end, start])
timetable.sort()

cnt = 0
end_now = 0
for time in timetable:
    start = time[1]
    end = time[0]
    if end_now <= start :
        end_now = end
        cnt += 1
print(cnt)