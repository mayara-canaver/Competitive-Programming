count = 0

while True:
    vezes = int(input())
    if vezes == 0:
        break
    if count > 0:
        print()
    lista = []
    for x in range(vezes):
        nomes = input()
        tipo, tamanho = list(input().split())
        if tamanho == "P":
            tamanho = "A"
        if tamanho == "M":
            tamanho = "B"
        if tamanho == "G":
            tamanho = "C"
        lista.append(" ".join([tipo, tamanho, nomes]))
    lista = sorted(lista)
    for string in lista:
        string = string.replace(" A ", " P ")
        string = string.replace(" B ", " M ")
        string = string.replace(" C ", " G ")
        print(string)
    count += 1