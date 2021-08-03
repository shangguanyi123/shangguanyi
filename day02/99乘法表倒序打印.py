for x in range(9,0,-1):
    for y in range(x,0,-1):
        print("%2d x%2d = %2d"%(x,y,x*y),end='\t')
    print()
