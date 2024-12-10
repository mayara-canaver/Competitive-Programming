lista = []
soma, media = 0, 0

while True:

    while True:

        numero = float(input())

        if numero < 0:
            break

        lista.append(numero)

    for x in lista:
        soma = soma + x

    media = soma/len(lista)

    print("%.2f" % media)

    break