from math import floor

qtd_tem = int(input())
qtd_galho = int(input())

faltam = floor(qtd_galho / 2)

if faltam - qtd_tem <= 0:
    print("Amelia tem todas bolinhas!")
else:
    print("Faltam %d bolinha(s)" % abs(qtd_tem - faltam))
