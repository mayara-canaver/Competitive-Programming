def pillars(num_pill, dist, width):
    resultado = ((num_pill - 1) * dist * 100) + ((num_pill - 2) * width)
    if resultado < 0:
        return 0
    else:
        return resultado