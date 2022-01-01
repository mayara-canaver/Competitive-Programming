while True:
    a, b = list(map(int, input().split()))

    if a == b == 0:
        break

    counta, lista = 0, []

    lista_perguntas = input().split()

    for pergunta in lista_perguntas:
        qtd = lista_perguntas.count(pergunta)

        if qtd >= b and pergunta not in lista:
            counta += 1

        lista.append(pergunta)

    print(counta)
