vezes = int(input())

for j in range(vezes):

    qt, s = list(map(int, input().split()))

    anterior = 250

    lista_valor_aluno = list(map(int, input().split()))

    for valor_aluno in lista_valor_aluno:
        auxiliar = abs(valor_aluno - s)

        if auxiliar < anterior:
            anterior = auxiliar
            indexo = lista_valor_aluno.index(valor_aluno) + 1

    print(indexo)
