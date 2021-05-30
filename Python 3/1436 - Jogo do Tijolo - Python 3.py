while True:
    a, b = input().split()

    if len(a) > len(b):
        b = b.rjust(len(a), "0")
    else:
        a = a.rjust(len(b), "0")

    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    if a == b == [0]:
        break
    cont = 0
    prox_numero = 1

    for x in range(len(a) -1, -1, -1):
        soma = a[x] + b[x]
        if soma >= 10:
            cont = cont + 1
            a[x-1] = a[x-1] + prox_numero
        else:
            pass

    if cont == 0:
        print("No carry operation.")
    elif cont == 1:
        print("1 carry operation.")
    else:
        print("%d carry operations." % cont)
