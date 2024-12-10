while True:
    try:
        h, m = list(map(int, input().split()))

        hora = h // 30
        minuto = m // 6

        if hora < 10:
            hora = str(hora)
            hora = "0" + hora

        hora = str(hora)

        if minuto < 10:
            minuto = str(minuto)
            minuto = "0" + minuto

        minuto = str(minuto)
        
        print(hora + ":" + minuto)

    except EOFError:
        break



