import sys
while True:

    try:
        soma = 0
        numero = int(input())
        if numero == 0:
            sys.exit()
        for x in range(numero+1):
            soma = soma + (x*x)

        print(soma)

    except EOFError:
        sys.exit()