import math

valor1 = input().split(" ")
valor1 = list(map(float, valor1))
valor2 = input().split(" ")
valor2 = list(map(float, valor2))

total = math.pow(valor1[0]-valor2[0], 2)+math.pow(valor1[1]-valor2[1], 2)

distancia = math.sqrt(total)
print("%.4f" %distancia)