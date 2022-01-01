import sys

while True:
    try:
        soma, x = 1, 1
        numero = int(input())
        while True:
            if x%numero == 0:
                break
            x = (x*10+1)%numero
            soma = soma + 1

        print(soma)

    except EOFError:
        sys.exit()