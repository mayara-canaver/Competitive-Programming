vezes = int(input())

lista = list(map(int, input().split()))

while len(lista) > 1:

    lista_aux = []

    for numero in range(len(lista) - 1):
        if lista[numero] + lista[numero + 1] == 0:
                lista_aux.append(1)
        else:
                lista_aux.append(-1)

    lista = lista_aux

if lista[0] != 1:
    print("preta")
else:
    print("branca")
