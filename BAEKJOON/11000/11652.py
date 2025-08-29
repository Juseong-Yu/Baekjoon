N = int(input())
dic = {}
for _ in range(N):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

max_count = max(dic.values())
candidate = []
for key, value in dic.items():
    if value == max_count:
        candidate.append(key)
print(min(candidate))