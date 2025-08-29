E, S, M = map(int,input().split())
i = 1
if E == 15:
  E = 0
if S == 28:
  S = 0
if M == 19:
  M = 0
while(True):
  if((i % 15 == E and i % 28 == S and i % 19 == M )):
    print(i)
    break
  i += 1