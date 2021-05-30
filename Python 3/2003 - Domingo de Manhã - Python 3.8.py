lista1, lista2 = [], []

for numero in range(15):
    if len(lista1) == 5:
        for y in range(len(lista1)):
            print("par[%d] = %d" % (y, lista1[y]))

        lista1 = []

    if len(lista2) == 5:
        for z in range(len(lista2)):
            print("impar[%d] = %d" % (z, lista2[z]))

        lista2 = []

    numero = int(input())

    if numero % 2 == 0:
        lista1.append(numero)
    else:
        lista2.append(numero)

for z1 in range(len(lista2)):
    print("impar[%d] = %d" % (z1, lista2[z1]))

for y1 in range(len(lista1)):
    print("par[%d] = %d" % (y1, lista1[y1]))

