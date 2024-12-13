lista = list(map(int, input().split()))

maximo = max(lista)

lista.remove(maximo)

maximo_de_novo = max(lista)

print(maximo_de_novo)
