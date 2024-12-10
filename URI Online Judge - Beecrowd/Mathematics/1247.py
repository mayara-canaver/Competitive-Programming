numero = int(input())

for x in range(1, numero+1):
    if x%2 == 0:
        total = 0
        total = pow(x,2)
        print("%d^2 = %d" % (x, total))