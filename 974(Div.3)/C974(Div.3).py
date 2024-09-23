t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n < 3:
        print("-1")
        continue
    sum1 = sum(a)
    avarage = sum1 /n
    count = 0
    max1 = max(a)
    for x in a:
        if x < avarage:
            count +=1
    if count/n < 0.5:
        
        pass
    else:
        print(0)

# (sum1 + x)/n > 