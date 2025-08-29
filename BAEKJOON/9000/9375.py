T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, group = input().split()
        if group in dic:
            dic[group].append(name)
        else:
            dic[group] = [name] 
    count = 1
    for idx in dic:
        count *= len(dic[idx]) + 1
    print(count-1)
