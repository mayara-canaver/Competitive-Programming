numero = int(input())

pecas = (numero * numero) // 2

if numero % 2 == 0:
    print("%d casas brancas e %d casas pretas" % (pecas, pecas))
else:
    print("%d casas brancas e %d casas pretas" % (pecas + 1, pecas))

