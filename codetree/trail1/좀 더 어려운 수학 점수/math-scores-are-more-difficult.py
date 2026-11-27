Am, Ae = map(int, input().split())
Bm, Be = map(int, input().split())

if Am == Bm:
    if Ae > Be :
        print("A")
    else:
        print("B")
else:
    if Am > Bm:
        print("A")
    else:
        print("B")