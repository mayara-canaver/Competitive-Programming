from sys import stdin

casos = int(stdin.readline())

for _ in range(casos):

    caso = list(input())
    contador = 1

    for caracter in caso:
        if caracter in ["A", "E", "I", "O", "S"] or caracter in ["a", "e", "i", "o", "s"]:
            contador *= 3
        else:
            contador *= 2

    print(contador)