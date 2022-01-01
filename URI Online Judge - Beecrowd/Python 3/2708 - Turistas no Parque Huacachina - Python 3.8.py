vezes = int(input())

numero = int(input())
count = numero
lista = []
lista2 = []

for x in range(vezes):
    competidor = int(input())
    lista.append(competidor)

lista = sorted(lista, reverse=True)

numerico = lista[numero - 1]

tamanho = lista[numero:].count(numerico)

total = tamanho + numero

print(total)
