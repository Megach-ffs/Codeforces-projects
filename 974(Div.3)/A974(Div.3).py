t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    r = 0
    count = 0
    for x in a:
        if x >= k:
            r += x
        else:
            if r > 0 and x == 0:
                r -=1
                count +=1
    print(count)

# lo = input().split()
# print(lo)
