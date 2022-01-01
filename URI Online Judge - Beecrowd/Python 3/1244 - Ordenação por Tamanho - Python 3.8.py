vezes = int(input())
lista = []

for x in range(vezes):
    pomekon = input()
    if pomekon not in lista:
        lista.append(pomekon)

quantidade = 151 - len(lista)
print("Falta(m) %d pomekon(s)." % quantidade)
