while True:
    try:
        vezes = int(input())
        for x in range(vezes):
            numero = int(input())
            numero = bin(numero)
            numero = str(numero)
            contar_1 = numero.count("1")
            print(contar_1)
    except EOFError:
        break
