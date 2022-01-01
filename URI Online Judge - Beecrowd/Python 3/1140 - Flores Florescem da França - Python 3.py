while True:
    numero_linha, numero_coluna, numero_instrucao = list(map(int, input().split()))

    conta_linha = 0

    if numero_linha == numero_coluna == numero_instrucao == 0:
        break

    lista_arena = []

    for x in range(numero_linha):
        linha = list(input())
        if "N" in linha:
            x = conta_linha
            y = linha.index("N")
            eh_n = True
        if "S" in linha:
            x = conta_linha
            y = linha.index("S")
            eh_s = True
        if "L" in linha:
            x = conta_linha
            y = linha.index("L")
            eh_l = True
        if "O" in linha:
            x = conta_linha
            y = linha.index("O")
            eh_o = True

        lista_arena.append(linha)
        conta_linha += 1

    instrucao = list(input())

    for parte in instrucao:
        if parte == "D":

        if parte == "E":

        if parte == "F":
            

    print(x, y)
    print(eh_n)

    print(lista_arena)
