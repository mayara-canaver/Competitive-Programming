from math import pi

vezes = int(input())

for x in range(vezes):
    n, ml = list(map(float, input().split()))
    rainho, raiao, altura = list(map(float, input().split()))

    qtd = ml / n

    alturinha = (3 * qtd) / (pi * (raiao ** 2 + raiao * rainho + rainho ** 2))

    print("%.2f" % alturinha)
