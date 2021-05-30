while True:
    try:
        lista_real, lista_final = [], []

        texto = input()

        if texto == "":
            print()
        else:
            texto = texto.replace(" ", "")
            texto = "".join(sorted(texto))

            lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

            for c in texto:
                lista_real.append(c)

            for c in lista:
                if c in lista_real:
                    lista_final.append(c)
                else:
                    lista_final.append("-")

            lista_final = "".join(lista_final)

            lista_final = lista_final.split("-")

            lista_final = list(filter(None, lista_final))

            for letra in lista_final:
                if letra != lista_final[-1]:
                    print("%s:%s, " % (letra[0], letra[-1]), end="")
                else:
                    print("%s:%s" % (letra[0], letra[-1]), end="\n")

    except EOFError:
        break
