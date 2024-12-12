lista = []

while True:
    try:
        nome = input()
        lista.append(nome)

    except EOFError:
        lista = sorted(lista, reverse=True, key=str.upper)
        print(lista[0])

        break

