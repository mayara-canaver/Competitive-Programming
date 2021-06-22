frase = input()

frase = frase + " "

frase = list(frase)

confere = True
lista = []
count = 0


for letra in range(len(frase)):
    if frase[letra] == "p" and frase[letra + 1] != "p":
        confere = True
    elif frase[letra] == "p" and frase[letra + 1] == "p" and confere == False:
        count += 1
    elif frase[letra] == "p" and frase[letra + 1] == "p" and confere:
        lista.append(frase[letra])
        confere = False
        letra += 1
    else:
        lista.append(frase[letra])

    if count == 1:
        confere = True
        count = 0

tamanho = len(lista)

lista = lista[:tamanho - 1]

print("".join(lista))