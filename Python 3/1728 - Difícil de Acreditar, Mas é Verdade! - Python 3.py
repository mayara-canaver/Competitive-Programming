from math import floor

while True:
    a, b, c = list(map(int, input().split()))

    if a == b == c == 0:
        break

    volume_total = a * b * c
    valor_aresta = volume_total ** (1 / 3)

    print(floor(valor_aresta))
