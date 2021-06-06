vezes = int(input())

for x in range(vezes):
    palavra = input()

    tamanho = len(palavra) / 100

    print("%.2f" % tamanho)
