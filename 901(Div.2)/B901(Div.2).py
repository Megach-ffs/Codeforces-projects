t = int(input())

for _ in range(t):
    n,m,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if k%2==1:
        k = 5

    else:
        k = 4
    for i in range(k):
        c =0 
        a.sort()
        b.sort()

        if (i+1)%2 == 1:
            if a[0]<b[-1]:
                c= a[0]
                a[0] = b[-1]
                b[-1] = c

        else:
            if a[-1]>b[0]:
                c= b[0]
                b[0] = a[-1]
                a[-1] = c


    print(sum(a))

