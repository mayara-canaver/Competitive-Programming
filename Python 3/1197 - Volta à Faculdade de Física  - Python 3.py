numero = int(input())

for x in range(numero):
    casas = int(input())
    grao = 1
    for y in range(casas):
        grao = grao*2
    kg = (grao//12)/1000
    print("%d kg" %kg)