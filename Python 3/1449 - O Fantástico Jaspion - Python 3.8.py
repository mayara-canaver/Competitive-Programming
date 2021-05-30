vezes = int(input())

for x in range(vezes):
    n1, n2 = list(map(int, input().split()))

    dicionario = {}

    for y in range(n1):
        chave = input()
        valor = input()
        dicionario[chave] = valor

    for z in range(n2):
        frase = list(input().split())

        for palavra in range(len(frase)):
            if frase[palavra] in dicionario:
                frase[palavra] = dicionario[frase[palavra]]

        print(" ".join(frase))

    if x != vezes:
        print()
