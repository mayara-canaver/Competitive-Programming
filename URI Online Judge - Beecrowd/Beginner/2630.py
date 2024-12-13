vezes = int(input())

for x in range(vezes):
    raio, w, h, x0, y0 = 0, 0, 0, 0, 0
    w, h, x0, y0 = list(map(int, input().split()))
    magia, nivel, cx, cy = list(input().split())
    nivel, cx, cy = int(nivel), int(cx), int(cy)

    if magia == "fire":
        if nivel == 1:
            raio = 20
        elif nivel == 2:
            raio = 30
        elif nivel == 3:
            raio = 50

    elif magia == "water":
        if nivel == 1:
            raio = 10
        elif nivel == 2:
            raio = 25
        elif nivel == 3:
            raio = 40

    elif magia == "earth":
        if nivel == 1:
            raio = 25
        elif nivel == 2:
            raio = 55
        elif nivel == 3:
            raio = 70

    else:
        if nivel == 1:
            raio = 18
        elif nivel == 2:
            raio = 38
        elif nivel == 3:
            raio = 60

    x_max, x_min, y_max, y_min, x_min_caixa, x_max_caixa, y_min_caixa, y_max_caixa = 0, 0, 0, 0, 0, 0, 0, 0

    x_max, x_min = cx + raio, cx - raio
    y_max, y_min = cy + raio, cy - raio

    x_min_caixa, x_max_caixa = x0, x0 + w
    y_min_caixa, y_max_caixa = y0, x0 + h

    if ((x_min_caixa <= x_min <= x_max_caixa) and (y_min_caixa <= y_min <= y_max_caixa)) and \
        ((x_min_caixa <= x_max <= x_max_caixa) and (y_min_caixa <= y_max <= y_max_caixa)):

        if magia == "fire":
            print(200)
        elif magia == "water":
            print(300)
        elif magia == "earth":
            print(400)
        elif magia == "air":
            print(100)
    else:
        print(0)
