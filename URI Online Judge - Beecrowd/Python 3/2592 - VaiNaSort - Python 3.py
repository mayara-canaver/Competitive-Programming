while True:
    casos = int(input())

    lst_inicial = []

    if casos == 0:
        break

    lst_inicial = [i + 1 for i in range(casos)]

    contador = 1

    while True:
        lst_final = list(map(int, input().split()))

        if lst_inicial == lst_final:
            break

        contador += 1

    print(contador)
