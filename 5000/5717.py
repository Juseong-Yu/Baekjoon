while True:
    B , G = map(int, input().split())
    if B == 0 and G == 0:
        break
    else:
        print(B + G)