A, B, C = map(int, input().split())
def modular(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (modular(A, B // 2, C)  ** 2) % C
    else:
        return modular(A, B - 1 , C) * (A % C) % C
    
print(modular(A, B, C))
