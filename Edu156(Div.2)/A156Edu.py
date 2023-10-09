t = int(input())
for _ in range(t):
    n = int(input())
    if n < 7:
        print("NO")
        continue
    powers = []
    while n > 0:
        power = 1
        while power <= n:
            power *= 3
        power //= 3
        powers.append(power)
        n -= power
    print("YES")
    print(*powers, "= ", len(powers))
