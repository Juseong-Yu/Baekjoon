L1 = int(input())
L2 = int(input())

L3 = (L2 % 10 )*L1
L4 = (L2 // 10 % 10) * L1
L5 = (L2 // 100 % 10) * L1
print(L3)
print(L4)
print(L5)
print(L3+L4*10+L5*100)