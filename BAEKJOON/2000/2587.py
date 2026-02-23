lst = []
for _ in range(5):
    N = int(input())
    lst.append(N)

total = sum(lst)
lst.sort()
print(total//5)
print(lst[2])