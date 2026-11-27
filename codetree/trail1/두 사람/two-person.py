Aage, Asex = input().split()
Bage, Bsex = input().split()

if (int(Aage) >= 19 and Asex == "M") or (int(Bage) >= 19 and Bsex == "M"):
    print(1)
else:
    print(0)