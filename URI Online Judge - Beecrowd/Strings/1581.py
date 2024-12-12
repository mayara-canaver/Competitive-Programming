vezes = int(input())

for x in range(vezes):
    numero = int(input())
    ano = 2015 - numero
    if ano == 0:
        print("1 A.C.")
    elif ano > 0:
        print("%d D.C." % ano)
    else:
        ano -= 1
        ano = abs(ano)
        print("%d A.C." % ano)
