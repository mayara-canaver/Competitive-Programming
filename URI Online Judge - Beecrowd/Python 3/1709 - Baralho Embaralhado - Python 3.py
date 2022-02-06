qtd_cartas = int(input())

numero = 1
cont = 0

while True:
    if numero <= qtd_cartas // 2:
        numero *= 2
    else:
        numero = 2 * (numero - qtd_cartas // 2) - 1

    if numero == 1:
        break

    cont += 1

print(cont + 1)
