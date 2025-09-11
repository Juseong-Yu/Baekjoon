a = int(input())
w, v = map(int, input().split())
A = w / v
if a <= A:
    print(1)
else:
    print(0)