a, b = list(map(int, input().split()))

distancia, variavel_a, variavel_b, voltas = 0, 0, 0, 0

while distancia < b:
    variavel_a += a
    variavel_b += b
    distancia = variavel_b - variavel_a
    voltas += 1

print(voltas)
