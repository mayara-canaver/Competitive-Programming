import sys

from math import hypot

try:
    while True:

        distancia = 0
        variaveis = 0
        variaveis = input().split()
        variaveis = list(map(int, variaveis))
        distancia = variaveis[0]
        vf = variaveis[1]
        vg = variaveis[2]

        tempo_guardinha = hypot(12, distancia)/ vg
        tempo_fugitivo = 12/vf

        if tempo_guardinha <= tempo_fugitivo:
            print("S")
        else:
            print("N")

except EOFError:
    sys.exit()
