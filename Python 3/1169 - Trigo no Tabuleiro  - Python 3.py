from math import sqrt

numero = int(input())
lista_d = []

for j in range(numero):
    numero_bolas, lista_d = 0, []
    numero_bolas = int(input())
    branca = input().split()
    branca = list(map(int, branca))
    x_branca, y_branca = branca[0], branca[1]

    for i in range(numero_bolas):
        distancia, numeros, distancia_minima, x, y = 0, 0, 0, 0, 0
        numeros = input().split()
        numeros = list(map(int, numeros))
        x, y = numeros[0], numeros[1]
        distancia = sqrt((x - x_branca) ** 2 + (y - y_branca) ** 2)
        lista_d.append(distancia)

    distancia_minima = lista_d.index(min(lista_d))
    distancia_minima = distancia_minima + 1
    print(distancia_minima)
