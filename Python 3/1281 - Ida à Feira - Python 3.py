alcool, diesel, gasolina = 0, 0, 0

while True:
    tipo = int(input())
    if tipo == 4:
        print("MUITO OBRIGADO")
        print("Alcool: %d" % alcool)
        print("Gasolina: %d" % gasolina)
        print("Diesel: %d" % diesel)
        break
    if tipo == 1:
        alcool = alcool + 1
    elif tipo == 2:
        gasolina = gasolina + 1
    elif tipo == 3:
        diesel = diesel + 1
    else:
        pass

