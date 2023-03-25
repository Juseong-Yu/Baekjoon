A,B,C = list(map(int,input().split()))
D = int(input())

C = C+D
B = (C//60)+B
C = C % 60
A = B // 60 +A
B  = B % 60
A = A % 24

print(A,B,C)