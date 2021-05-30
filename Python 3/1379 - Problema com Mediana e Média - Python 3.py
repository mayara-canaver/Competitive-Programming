

nota_cem, nota_cinq, nota_vint, nota_dez, nota_cin, nota_dois, nota_um = 0, 0, 0, 0, 0, 0, 0

valor = int(input())

numero = valor

if valor/100 > 0:
    nota_cem = valor // 100
    valor = valor - nota_cem*100
if valor/50 > 0:
    nota_cinq = valor // 50
    valor = valor - nota_cinq*50
if valor/20 > 0:
    nota_vint = valor // 20
    valor = valor - nota_vint*20
if valor/10 > 0:
    nota_dez = valor // 10
    valor = valor - nota_dez*10
if valor/5 > 0:
    nota_cin = valor // 5
    valor = valor - nota_cin*5
if valor / 2 > 0:
    nota_dois = valor // 2
    valor = valor - nota_dois*2

nota_um = valor

print(numero)
print("%d nota(s) de R$ 100,00" % nota_cem)
print("%d nota(s) de R$ 50,00" % nota_cinq)
print("%d nota(s) de R$ 20,00" % nota_vint)
print("%d nota(s) de R$ 10,00" % nota_dez)
print("%d nota(s) de R$ 5,00" % nota_cin)
print("%d nota(s) de R$ 2,00" % nota_dois)
print("%d nota(s) de R$ 1,00" % nota_um)
