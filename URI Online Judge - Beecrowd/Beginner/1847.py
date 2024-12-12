def verifica_par_impar(pulo, n, inicio):
    if pulo%2 == 0:
        inicio = (inicio-(pulo - 1))%n
        return inicio

    else:
        inicio = (inicio+(pulo - 1))%n
        return inicio

while True:
    lista_nome, lista_valor = [], []
    crianca = int(input())

    if crianca == 0:
        break

    for x in range(crianca):
        dados = input().split()
        nome, valor = dados[0], dados[1]
        valor = int(valor)

        lista_nome.append(nome)
        lista_valor.append(valor)


    inicio = 1
    pulo = lista_valor[0]
    n = len(lista_valor)
    if pulo%2 == 0:
        inicio = n - 1

    while len(lista_nome)>1:

        inicio = verifica_par_impar(pulo, n, inicio)
        pulo = lista_valor[inicio]
        lista_valor.pop(inicio)
        lista_nome.pop(inicio)
        n = len(lista_valor)
        if pulo%2 == 1:
            inicio = inicio%n
        else:
            inicio = (inicio-1)%n

    print("Vencedor(a): %s" % lista_nome[0])