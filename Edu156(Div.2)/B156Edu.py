t = int(input())

for _ in range(t):

    px,py = map(int, input().split())
    ax,ay = map(int, input().split())
    bx,by = map(int, input().split())
    if (ax ** 2 + ay ** 2) ** 0.5< (bx ** 2 + by ** 2) ** 0.5:
        minx,miny = ax,ay
    else:
        minx,miny = bx,by
    
    if ((px-ax )** 2 + (py-ay) ** 2) ** 0.5< ((px-bx) ** 2 + (py-by) ** 2) ** 0.5:
        minpx,minpy = ax,ay
    else:
        minpx,minpy = bx,by

    if minpx == minx and minpy==miny:
        print(((px-minx)**2+(py-miny)**2)**0.5)
    else:
        if (((ax-bx)**2+(ay-by)**2)**0.5)/2 < ((px**2+py**2)**0.5):
            print((((ax-bx)**2+(ay-by)**2)**0.5)/2)
        else:
            print(((px-minx)**2+(py-miny)**2)**0.5)

    