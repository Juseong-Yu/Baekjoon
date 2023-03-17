T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    list2 = []
    for p in range(k):
        for j in range(n):
            adder = 0
            for m in range(j+1):
                adder += list1[m]
            list2.append(adder)
        list1 = list2
        list2 = []
    print(list1[-1])