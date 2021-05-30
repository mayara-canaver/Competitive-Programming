dicionario = {"W": 1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T": 1/32, "X": 1/64}

while True:
    frase = list(input().split("/"))
    if len(frase) == 1:
        break
    count = 0
    for x in frase[1: -1]:
        soma = 0
        for y in x:
            soma += dicionario.get(y)
        if soma == 1:
            count += 1
    print(count)
