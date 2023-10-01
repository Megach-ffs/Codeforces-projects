t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    first_sum = (k * (k + 1)) // 2
    last_sum = (n * (n + 1)) // 2 - ((n - k) * (n - k + 1)) // 2

    if first_sum <= x <= last_sum:
        print("YES")
    else:
        print("NO")