N,M,Q = input().split(" ")
int(N)
int(M)
int(Q)

corps = []
for i in range(N):
  G,H,P = input().split(" ")
  corps.append([int(G),str(H),int(P)])
print(corps)

M_in = []
for i in range(Q):
  inQ = input()
  if Q == "6":
    print(M)
  elif Q == "7":
    result = 0
    for k in range(len(M_in)):
      result += M_in[k][1]
    print(M + M_in)
  else:
    inQ, corp, h_m = inQ.split(" ")
    if inQ == 1:
      for 
