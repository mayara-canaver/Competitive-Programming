vezes = int(input())

for numero in range(vezes):
    lista = []
    numero = int(input())
    for x in range(numero):
        x = input()
        lista.append(x)

    if len(set(lista)) != 1:
        print("ingles")
    else:
        print(x)


