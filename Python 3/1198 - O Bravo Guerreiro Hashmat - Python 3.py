import sys
import math

pi = 3.1415926535897
perimetro, heron, r  = 0, 0, 0

while True:

    try:

        numero = input().split()
        numero = list(map(int, numero))

        a, b, c = numero

        p = (a + b + c) / 2
        area_triangulo = math.sqrt(p*(p-a)*(p-b)*(p-c))

        raio_externo = (a*b*c)/math.sqrt((a+b+c) * (b+c-a) * (c+a-b) * (a+b-c))
        area_circulo_maior = pi*(raio_externo*raio_externo)

        raio_interno = area_triangulo/p
        area_circulo_menor = pi*(raio_interno*raio_interno)

        area_t = area_triangulo - area_circulo_menor
        area_c_maior = area_circulo_maior - area_triangulo

        print("%.4f %.4f %.4f" % (area_c_maior, area_t, area_circulo_menor))

    except EOFError:
        sys.exit()