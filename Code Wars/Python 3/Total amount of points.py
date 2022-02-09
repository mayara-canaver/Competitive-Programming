def points(games):
    
    total = 0

    for partida in games:
        time_a, time_b = partida.split(":")

        if int(time_a) > int(time_b):
            total += 3
        elif int(time_a) < int(time_b):
            pass
        else:
            total += 1

    return total