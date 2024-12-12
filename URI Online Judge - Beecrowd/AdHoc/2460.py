while True:
    try:
        vezes = 0
        lista = []

        vezes = int(input())
        for x in range(vezes):
            numero = input()
            lista.append(numero)

        lista = sorted(lista)

        for y in lista:
            print(y)

    except EOFError:
        break
