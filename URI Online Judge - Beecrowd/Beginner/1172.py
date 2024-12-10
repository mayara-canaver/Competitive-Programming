numero = int(input())
x, y, z = 1, 2, 3

for vezes in range(numero):
    print("%d %d %d PUM" % (x, y, z))
    x = x + 4
    y = y + 4
    z = z + 4