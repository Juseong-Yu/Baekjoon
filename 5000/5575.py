A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))


A_tmp = (A[0]*60*60 + A[1]*60 + A[2]) - (A[3]*60*60 + A[4]*60 + A[5])
B_tmp = (B[3]*60*60 + B[4]*60 + B[5]) - (B[0]*60*60 + B[1]*60 + B[2])
C_tmp = (C[3]*60*60 + C[4]*60 + C[5]) - (C[0]*60*60 + C[1]*60 + C[2])

A_hour = int(A_tmp / 60 / 60)
A_tmp = int(A_tmp - A_hour * 60 * 60)
A_min = int(A_tmp / 60)
A_sec = int(A_tmp - A_min * 60)

B_hour = int(B_tmp / 60 / 60)
B_tmp = int(B_tmp - B_hour * 60 * 60)
B_min = int(B_tmp / 60)
B_sec = int(B_tmp - B_min * 60)

C_hour = int(C_tmp / 60 / 60)
C_tmp = int(C_tmp - C_hour * 60 * 60)
C_min = int(C_tmp / 60)
C_sec = int(C_tmp - C_min * 60)

print(A_hour,A_min,A_sec)
print(B_hour,B_min,B_sec)
print(C_hour,C_min,C_sec)