while True:
    try:
        a, b = float(input()), float(input())
        area_circulo = 3.14 * ((b / 2)**2)
        altura = a / area_circulo
        print("ALTURA = %.2f" % altura)
        print("AREA = %.2f" % area_circulo)
    except EOFError:
        break
