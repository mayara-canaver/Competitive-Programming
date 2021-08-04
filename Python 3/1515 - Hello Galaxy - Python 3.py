while True:
    lista_aux = []
    vezes = int(input())

    if vezes == 0:
        break

    lista_numeros = list(map(int, input().split()))
    lista_aux = lista_numeros.copy()

    maximo = max(lista_numeros)
    lista_numeros.remove(maximo)
    maximo_2 = max(lista_numeros)

    indexo = lista_aux.index(maximo_2)

    print(indexo + 1)
