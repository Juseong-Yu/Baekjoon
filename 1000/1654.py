k,n = list(map(int,input().split()))
rope = []
for i in range(k):
    d = int(input())
    rope.append(d)


def count_rope(lst,cm):
    count = 0
    for l in lst:
        if l == 0:
            continue
        count += l//cm
    return count

def result(rope,n,left,right):
    tmp = (left+right)//2
    if tmp == 0:
        return 1
    count1 = count_rope(rope,tmp) 
    count2 = count_rope(rope,tmp+1)
    if count1 >= n and count2 < n:
        return tmp
    elif count1 < n:
        return result(rope,n,left,tmp)
    elif count2 >= n:
        return result(rope,n,tmp+1,right)

print(result(rope,n,0,max(rope)))
print(1)