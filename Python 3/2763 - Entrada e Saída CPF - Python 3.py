while True:
    try:
        texto = input()

        confere = True
        conferiu = True

        for caracter in texto:
            if caracter == "_":
                if confere:
                    print("<i>", end="")
                else:
                    print("</i>", end="")
                confere = not confere
            elif caracter == "*":
                if conferiu:
                    print("<b>", end="")
                else:
                    print("</b>", end="")
                conferiu = not conferiu
            else:
                print(caracter, end="")

        print()

    except EOFError:
        break
