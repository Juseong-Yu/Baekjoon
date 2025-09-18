N = int(input())
A = list(map(int, input().split()))
M = int(input())
Q = []
results = [None] * M
ks = 1
for idx in range(M):
    m = list(map(int, input().split()))
    if m[0] == 1:
        Q.append((1, ks - 0.1, m[1], m[2], idx))
        ks += 1
    else:
        Q.append((2, m[1], m[2], m[3], idx))
Q.sort(key=lambda x: x[1])
print(Q)
for q, k, i, j, idx in Q:
    if q == 2:
        results[idx] = sum(A[i : j + 1])
    else:
        A[i - 1] = j

for result in results:
    if result != None:
        print(result)