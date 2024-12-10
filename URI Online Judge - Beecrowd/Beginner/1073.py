lista = []

for x in range(100):
    numero = int(input())
    lista.append(numero)
    maior = max(lista)

final = lista.index(maior)
final = final + 1
print(maior)
print(final)
