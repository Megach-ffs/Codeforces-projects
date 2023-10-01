t = int(input())

for _ in range(t):
        
    n = int(input())
    
    arr = list(range(6, n + 6))

    for i in range(n - 2):
        arr[i + 2] = arr[i+1] + (3*arr[i+2])//(arr[i]+arr[i+1]) + 1

    print(*arr)
    