while True:
    try:

        lst_vogais = list(input())
        frase = input()

        contador = 0

        for vogal in lst_vogais:
            if vogal in frase:
                contador += frase.count(vogal)

        print(contador)

    except EOFError:
        break
