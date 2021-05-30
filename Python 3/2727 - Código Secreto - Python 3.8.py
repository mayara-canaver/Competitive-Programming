while True:
    try:
        hora, minuto = list(map(int, input().split(":")))
        hora *= 60
        minuto += 60
        total = hora + minuto
        novahora  = (total - 480)
        if novahora < 0:
            novahora = 0
        print("Atraso maximo: %d" % novahora)

    except EOFError:
        break
