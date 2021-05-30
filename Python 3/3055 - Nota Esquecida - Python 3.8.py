dia1, dia2 = list(map(int, input().split()))

prazo_final = dia2 - 3

while True:
    if dia1 > dia2:
        print("Eu odeio a professora!")
        break

    if dia1 <= prazo_final:
        print("Muito bem! Apresenta antes do Natal!")
        break
    else:
        print("Parece o trabalho do meu filho!")
        dia1 += 2

    if dia1 < 24:
        print("TCC Apresentado!")
        break
    else:
        print("Fail! Entao eh nataaaaal!")
        break
