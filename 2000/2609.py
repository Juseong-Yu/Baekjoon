A, B = list(map(int,input().split()))

if A < B :
    A,B = B,A

A1 = A
A2 = A
B1 = B
B2 = B

r = B
while A1 % B1 != 0:
    r = A1 % B1
    A1= B1
    B1 = r

print(r)

tmp = 0

while True:
    tmp += 1
    if (A2*tmp) % B2 == 0:
        print(A2*tmp)
        break