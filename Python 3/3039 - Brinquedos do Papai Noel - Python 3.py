vezes = int(input())

for x in range(vezes):

    dicionario = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                  "m": 0,
                  "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
                  "z": 0}

    frase = input()
    frase = frase.lower()

    lista_abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    lista_abc_valor = []

    for letrona in lista_abc:
        lista_abc_valor.append(frase.count(letrona))

    listinha = []
    maximo = max(lista_abc_valor)

    for x, c in zip(lista_abc, lista_abc_valor):
        if c == maximo:
            listinha.append(x)

    variavel = "".join(listinha)

    print(variavel)
