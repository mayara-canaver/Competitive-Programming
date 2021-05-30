numero = int(input())
x, y, z = 1, 1, 1

for vezes in range(1, numero+1):

    y = pow(vezes, 2)
    z = pow(vezes, 3)

    print("%d %d %d" % (x, y, z))
    x = vezes + 1