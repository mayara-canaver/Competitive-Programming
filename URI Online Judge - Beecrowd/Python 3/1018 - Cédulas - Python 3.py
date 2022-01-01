nota_cem, nota_cinq, nota_vint, nota_dez, nota_cin, nota_dois, nota_um = 0, 0, 0, 0, 0, 0, 0
mnota_cem, mnota_cinq, mnota_vint, mnota_dez, mnota_cin, mnota_dois, mnota_um = 0, 0, 0, 0, 0, 0, 0

valor = int(input().replace(".", ""))

if valor/10000 > 0:
    nota_cem = valor // 10000
    valor = valor - nota_cem*10000

if valor/5000 > 0:
    nota_cinq = valor // 5000
    valor = valor - nota_cinq*5000

if valor/2000 > 0:
    nota_vint = valor // 2000
    valor = valor - nota_vint*2000

if valor/1000 > 0:
    nota_dez = valor // 1000
    valor = valor - nota_dez*1000

if valor/500 > 0:
    nota_cin = valor // 500
    valor = valor - nota_cin*500

if valor / 200 > 0:
    nota_dois = valor // 200
    valor = valor - nota_dois*200

if valor/100 > 0:
    mnota_cem = valor // 100
    valor = valor - mnota_cem*100

if valor/50 > 0:
    mnota_cinq = valor // 50
    valor = valor - mnota_cinq*50

if valor/25 > 0:
    mnota_vint = valor // 25
    valor = valor - mnota_vint*25

if valor/10 > 0:
    mnota_dez = valor // 10
    valor = valor - mnota_dez*10

if valor/5 > 0:
    mnota_cin = valor // 5
    valor = valor - mnota_cin*5

mnota_dois = valor

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % nota_cem)
print("%d nota(s) de R$ 50.00" % nota_cinq)
print("%d nota(s) de R$ 20.00" % nota_vint)
print("%d nota(s) de R$ 10.00" % nota_dez)
print("%d nota(s) de R$ 5.00" % nota_cin)
print("%d nota(s) de R$ 2.00" % nota_dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % mnota_cem)
print("%d moeda(s) de R$ 0.50" % mnota_cinq)
print("%d moeda(s) de R$ 0.25" % mnota_vint)
print("%d moeda(s) de R$ 0.10" % mnota_dez)
print("%d moeda(s) de R$ 0.05" % mnota_cin)
print("%d moeda(s) de R$ 0.01" % mnota_dois)
