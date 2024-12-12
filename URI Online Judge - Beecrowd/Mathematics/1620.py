vezes = int(input())

lista = list(map(int, input().split()))

distancia, distancia_nova = 0, ""
confere1, confere2 = False, False
count = 0

if len(lista) == 1:
    count = 1
else:

    for x in range(len(lista) - 1):
        distancia = lista[x + 1] - lista[x]

        if distancia == distancia_nova:
            confere1 = True
        else:
            confere1 = False
            if confere2 == False:
                count += 1

        distancia_nova = distancia

print(count)
