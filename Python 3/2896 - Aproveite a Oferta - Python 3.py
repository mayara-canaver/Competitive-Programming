anterior = 0
proximo = 0

vezes = int(input())
lista = []

while(vezes != 0):
    proximo = proximo + anterior
    anterior = proximo - anterior
    if (proximo == 0):
        proximo = proximo + 1

    lista.append(str(proximo))

    vezes -= 1

lista = lista[:: -1]

print(" ".join(lista))
