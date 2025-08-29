T = int(input())
for i in range(T):
    H_n=1
    W_n=1
    H,W,N = list(map(int,input().split()))

    for j in range(N-1):
        if H_n == H:
            H_n = 1
            W_n += 1
        else:
            H_n +=1

    if W_n >= 10:
        print(str(H_n)+str(W_n))
    else:
        print(str(H_n)+'0'+str(W_n))
