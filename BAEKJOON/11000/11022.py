T = int(input())
for i in range(T):
    A,B = list(map(int,input().split()))
    print("Case #{}: {} + {} = {}".format(i+1,A,B,A+B))