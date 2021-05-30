while True:
    a, b, resposta, media = -1, -1, 0, 0
    while a < 0 or a > 10:
        a = float(input())
        if a < 0 or a > 10:
            print("nota invalida")
    while b < 0 or b > 10:
        b = float(input())
        if b < 0 or b > 10:
            print("nota invalida")
    media = (a + b) / 2
    print("media = %.2f" % media)
    while True:
        print("novo calculo (1-sim 2-nao)")
        resposta = int(input())
        if resposta == 1 or resposta == 2:
            break
    if resposta == 1:
        pass
    else:
        break



