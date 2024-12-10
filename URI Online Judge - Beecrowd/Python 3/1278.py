import re

count = 0

while True:
    casos = int(input())

    if casos == 0:
        break

    if count > 0:
        print()

    lst_linhas = []

    for caso in range(casos):
        linha = input()
        linha = re.sub(" {2,}", " ", linha).strip()
        lst_linhas.append(linha)

    maximo = max(map(len, lst_linhas))

    for frase in lst_linhas:
        print(frase.rjust(maximo))

    count += 1
