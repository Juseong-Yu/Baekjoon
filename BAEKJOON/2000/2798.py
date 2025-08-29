N, M = list(map(int,input().split()))
L = list(map(int,input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if L[i]+L[j]+L[k] <= M and result < L[i]+L[j]+L[k]:
                result = L[i]+L[j]+L[k]
            if result == M:
                break

print(result)