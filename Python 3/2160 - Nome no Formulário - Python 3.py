lista = ["j", "s", "p", "v", "b", "x", "z", "J", "S", "P", "V", "B", "X", "Z"]

while True:
    try:
        texto = input()

        aux = ""

        for caracter in texto:

            if caracter in lista:

                caracter = "f"

                if caracter == "F" and aux == "F":
                    print("", end="")
                elif caracter == "f" and aux == "F":
                    print("", end="")
                elif caracter == "f" and aux == "f":
                    print("", end="")
                elif caracter == "F" and aux == "f":
                    print("", end="")
                else:
                    pass

            else:
                print(caracter, end="")

            aux = caracter

        print()

    except EOFError:
        break
