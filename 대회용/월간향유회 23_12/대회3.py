N,M,Q = input().split(" ")
int(N)
int(M)
int(Q)

corps = []
for i in range(N):
  G,H,P = input().split(" ")
  corps.append([int(G),str(H),int(P)])
print(corps)