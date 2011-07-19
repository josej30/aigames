def refreshMap(mm):

    for i in range(0,len(mm.m)):
        for j in range(0,len(mm.m)):
            if (mm.m[i][j]!=-1) and (mm.m[i][j]<20):
                mm.m[i][j]+=2
            elif mm.m[i][j]>20:
                mm.m[i][j]=20
                
