import sys

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

while True:

    try:
        numero = input().split()
        numero = list(map(int, numero))

        a, b = numero

        perimetro = (a + b) * 2


        if a == b:
            resultado = perimetro//a
            print(resultado)
        else:
            resultado = perimetro//mdc(a, b)
            print(resultado)

    except EOFError:
        sys.exit()

