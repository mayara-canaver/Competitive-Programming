notas = input()
notas = list(notas)

lista = []

for x in range(len(notas) - 1):
    if notas[x + 1] == "0":
        nota_10 = int(notas[x] + "0")
        lista.append(nota_10)
    else:
        lista.append(int(notas[x]))
        if 0 in lista:
            lista.remove(0)

if notas[-1] != "0":
    lista.append(int(notas[-1]))

media = sum(lista) / len(lista)
print("%.2f" % media)
