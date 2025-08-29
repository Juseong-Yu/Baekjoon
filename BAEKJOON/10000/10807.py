num=int(input())
nums=list(map(int,input().split()))
n=int(input())
score=0
for i in range(num):
    if n==nums[i]:
        score +=1
print(score)