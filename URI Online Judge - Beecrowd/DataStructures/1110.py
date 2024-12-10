while True:
    cartas = int(input())

    if cartas == 0:
        break

    lst_cartas = [carta for carta in range(cartas, 0, -1)]
    lst_cartas_dropadas = []

    while len(lst_cartas) != 1:

        lst_cartas_dropadas.append(lst_cartas[-1])

        lst_cartas.pop()

        lst_cartas.insert(0, lst_cartas[-1])

        if len(lst_cartas) == 1:
            break

        lst_cartas.pop()

    print("Discarded cards: ", end="")
    print(*lst_cartas_dropadas, sep=", ")
    print("Remaining card: %d" % lst_cartas[0])
