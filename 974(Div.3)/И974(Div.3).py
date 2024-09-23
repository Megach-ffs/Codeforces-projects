t = int(input())

for _ in range(t):
    n, k = map(int, input().split()) 

    if ((n + 1) // 2 - (n-k+1) // 2)%2==0:
        print("YES")
    else:
        print("NO")

1000
k=3
997
998
999
1000
