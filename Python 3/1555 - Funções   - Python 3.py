lista = []

for rotacao in range(10):
    numero = int(input())
    if numero <= 0 : numero = 1
    lista.append(numero)
    print("X[%d] = %d" % (rotacao, numero))


