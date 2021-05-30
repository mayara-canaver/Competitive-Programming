import sys

while True:
    try:

        palavra = []

        alfabeto = input()
        lampada = int(input())
        numeros = input().split()
        numeros = list(map(int, numeros))
        for x in numeros:
            palavra.append(alfabeto[x-1])
        print("".join(palavra))
    except EOFError:
        sys.exit()