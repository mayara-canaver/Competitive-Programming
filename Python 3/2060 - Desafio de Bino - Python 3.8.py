while True:
    try:
        mes, dia = list(map(int, input().split()))
        mes_natal, dia_natal = 12, 25
        mes_total = mes_natal - mes

        if mes_total == 0 and dia == 25:
            print("E natal!")
        elif mes_total == 0 and dia == 25:
            print("E vespera de natal!")
        elif mes_total == 0 and dia > 24:
            print("Ja passou!")
        else:
            dia_total = dia_natal - dia
            if dia_total < 0:
                dia_total = 25 - abs(dia_total)
                dia_total += (mes_total * 30) - 25
            else:
                dia_total += (mes_total * 30)

            if mes_total == 2 or mes_total == 3:
                dia_total += 1
            if mes_total == 4:
                dia_total += 2
            if mes_total == 5 or mes_total == 6:
                dia_total += 3
            if mes_total == 7 or mes_total == 8:
                dia_total += 4
            if mes_total == 9:
                dia_total += 5
            if mes_total == 10:
                dia_total += 4
            if mes_total == 11:
                dia_total += 5

            if dia_total == 1:
                print("E vespera de natal!")
            else:
                print("Faltam %d dias para o natal!" % dia_total)

    except EOFError:
        break
