x, y = list(map(int, input().split()))

for a in range(1, y + 1, x):
    for b in range(0, x+1):
        if b == x-1:
            print("%d" % (a + b))
            break
        print("%d " % (a + b), end="")
