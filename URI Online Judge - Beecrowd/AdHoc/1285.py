from math import ceil

while True:
    try:
        n, m = list(map(int, input().split()))

        contador = 0

        for numero in range(n, m + 1):

            numero = str(numero)

            if len(numero) == len(set(numero)):
                contador += 1

        print(contador)

    except EOFError:
        break
