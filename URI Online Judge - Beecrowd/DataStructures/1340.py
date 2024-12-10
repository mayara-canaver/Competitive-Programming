vezes = int(input())
a, b, c = 1, 1, 1

for x in range(1, vezes + 1):
    b = a ** 2
    c = a ** 3
    print("%d %d %d" % (a, b, c))
    b += 1
    c += 1
    print("%d %d %d" % (a, b, c))
    a += 1