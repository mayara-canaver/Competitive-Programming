tamanho = int(input())

tabuleiro = []
count = 0
confere = True

for linha in range(tamanho):
    fileira = input()

    if confere:
        tabuleiro += fileira
    else:
        fileira = fileira[:: -1]
        tabuleiro += fileira

    confere = not confere

tabuleiro = "".join(tabuleiro)

tabuleiro = tabuleiro.split("A")

listinha = []

for posicao in tabuleiro:
    count = posicao.count("o")
    listinha.append(count)

maximo = max(listinha)

print(maximo)
