t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k not in a:
        print("NO")
        continue
    cont = a.count(k)
    max=1
    for x in a:
        cont1 = a.count(x)
        if cont1>cont:
            max1=0
            break

    if max == 1:
        print("YES")
    else:
        print("NO")
        