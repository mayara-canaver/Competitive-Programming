from math import tan, radians
import sys

while True:
    try:
        numeros = input().split()
        numeros = list(map(float, numeros))
        ang, dist, altura = numeros[0], numeros[1], numeros[2]

        angulo = ang*3.141592654/180

        angulo = tan(angulo)
        altura_arvore = angulo*dist

        altura_arvore = altura_arvore + altura

        altura_arvore = altura_arvore*5

        print("%.2f" %altura_arvore)

    except EOFError:
        sys.exit()