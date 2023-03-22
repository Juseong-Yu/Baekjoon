while True:
    try:
        x1,y1,x2,y2,x3,y3,x4,y4 = list(map(float,input().split()))
        
        if (x1 == x2 and y1 == y2):
            xtmp3 = x1
            ytmp3 = y1
            xtmp1 = x3
            ytmp1 = y3
            xtmp2 = x4
            ytmp2 = y4

        if (x1 == x3 and y1 == y3):
            xtmp3 = x1
            ytmp3 = y1
            xtmp1 = x2
            ytmp1 = y2
            xtmp2 = x4
            ytmp2 = y4

        if (x1 == x4 and y1 == y4):
            xtmp3 = x1
            ytmp3 = y1
            xtmp1 = x3
            ytmp1 = y3
            xtmp2 = x2
            ytmp2 = y2

        if (x2 == x3 and y3 == y2):
            xtmp3 = x2
            ytmp3 = y2
            xtmp1 = x1
            ytmp1 = y1
            xtmp2 = x4
            ytmp2 = y4
        
        if (x2 == x4 and y4 == y2):
            xtmp3 = x2
            ytmp3 = y2
            xtmp1 = x1
            ytmp1 = y1
            xtmp2 = x3
            ytmp2 = y3
        
        if (x4 == x3 and y3 == y4):
            xtmp3 = x3
            ytmp3 = y3
            xtmp1 = x1
            ytmp1 = y1
            xtmp2 = x2
            ytmp2 = y2

        xp = (xtmp1+xtmp2) / 2
        yp = (ytmp1+ytmp2) / 2
        xr = (2*xp)-xtmp3
        yr = (2*yp)-ytmp3
        print('%.3f %.3f' %(xr,yr))
    except EOFError:
        break