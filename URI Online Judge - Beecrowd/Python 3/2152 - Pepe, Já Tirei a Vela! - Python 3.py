testes = int(input())

for teste in range(testes):
    hora, minuto, ocorrencia = list(map(int, input().split()))

    if hora < 10:
        hora = "0" + str(hora)

    if minuto < 10:
        minuto = "0" + str(minuto)

    if ocorrencia == 1:
        print("%s:%s - A porta abriu!" % (hora, minuto))
    else:
        print("%s:%s - A porta fechou!" % (hora, minuto))
