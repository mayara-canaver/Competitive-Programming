while True:
    try:
        numero = int(input())

        print(numero - 1)

    except EOFError:
        break
