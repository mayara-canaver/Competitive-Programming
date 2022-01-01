while True:
    try:
        vezes = int(input())
        lista = []

        for x in range(vezes):
            tempo = float(input())
            lista.append(tempo)

        print(min(lista))

    except EOFError:
        break
