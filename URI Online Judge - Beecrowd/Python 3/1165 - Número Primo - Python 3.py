while True:
    try:
        real = input()
        centavo = input()
        if len(centavo) == 1:
            centavo = "0" + centavo
        valor = real + "." + centavo
        valor = float(valor)
        valor_convertido = "${:,.2f}".format(valor)
        print(valor_convertido)

    except EOFError:
        break
