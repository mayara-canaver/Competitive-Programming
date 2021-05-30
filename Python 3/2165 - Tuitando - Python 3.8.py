vezes = int(input())

for frase in range(vezes):
    frase = input()
    tamanho = int((len(frase)) / 2)
    frase1 = frase[:tamanho]
    frase2 = frase[tamanho:]
    frase1 = frase1[::-1]
    frase2 = frase2[::-1]
    print("%s%s" % (frase1, frase2))
