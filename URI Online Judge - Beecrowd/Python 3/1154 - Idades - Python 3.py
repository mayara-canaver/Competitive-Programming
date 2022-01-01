import sys

qtd = 0

while True:

    try:
        numero = input().split()
        numero = list(map(int, numero))
        a, b = numero

        if a > b:
            qtd = a - b
            print(qtd)
        else:
            qtd = b - a
            print(qtd)

    except EOFError:
        sys.exit()