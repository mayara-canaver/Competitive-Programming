while True:
    pontos = float(input())

    i = 2 * pontos - 3

    if pontos == 0:
        break

    x = (i - pontos) / pontos

    print("%.6f" % x)
