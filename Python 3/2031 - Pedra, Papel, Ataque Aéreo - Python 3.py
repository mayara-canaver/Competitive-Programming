while True:
    try:
        vezes = int(input())
        soma = 0
        lista1, lista2, lista3 = [], [], []
        for x in range(vezes):
            t, c = list(map(int, input().split()))
            lista1.append(t)
            lista2.append(c)
            valor = t - c
            if valor < 0:
                valor = abs(valor)
            lista3.append(valor)
        maximo = max(lista3)
        tirar = lista3.index(maximo)
        del lista1[tirar]
        del lista2[tirar]
        print(lista2)
        soma += sum(lista2)
        print(soma)
    except EOFError:
        break
