t = int(input())
    
for _ in range(t):
    n,m = map(int, input().split())
    x = input()
    s = input()
    count = 0
    while True:
        # print(x)
        if s in x:
            break
        if len(x) > 25: # if count > 25:
            count = -1
            break
        x = x+x
        count+=1
    
    print(count)