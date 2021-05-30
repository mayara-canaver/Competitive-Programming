vezes = int(input())
lista = []

for numero in range(vezes):
    numero = int(input())
    lista.append(numero)

carlos = lista[0]
maximo = max(lista)

if carlos == maximo:
    print("S")
else:
    print("N")
