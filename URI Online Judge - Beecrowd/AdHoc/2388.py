vezes = int(input())

lista = []

for x in range(vezes):
    numero = int(input())
    lista.append(numero)

nova_lista = set(lista)

nova_lista = sorted(nova_lista)

for x in nova_lista:
    contador = lista.count(x)
    print("%d aparece %d vez(es)" % (x, contador))
