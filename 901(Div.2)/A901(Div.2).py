import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b, n = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    for y in range(len(x)):
        if x[y]>=a:
            x[y] = a - 1

    print(sum(x)+(b))


