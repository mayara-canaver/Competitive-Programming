while True:
    try:
        palavra = input()

        if palavra == "esquerda":
            print("ingles")
        elif palavra == "direita":
            print("frances")
        elif palavra == "nenhuma":
            print("portugues")
        else:
            print("caiu")

    except EOFError:
        break
