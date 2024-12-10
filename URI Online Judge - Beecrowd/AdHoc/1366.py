vezes = int(input())

for x in range(vezes):
    count = 0
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

    frase = list(input().lower())

    for caracter in frase:
        if caracter in alfabeto:
            alfabeto.remove(caracter)
            count += 1

    if count == 26:
        print("frase completa")
    elif count >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
