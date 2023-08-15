E = int(input())
S = int(input())
M = int(input())

for i in range(1,7981):
  if ((i%15 == E & i%28 == S & i%19 == M) | i == 7980):
    print(i)
    break

