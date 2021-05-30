from decimal import Decimal

while True:
    numero = input()
    if numero.startswith("0x"):
        numero_final = int(numero, 16)
        print(numero_final)
    elif int(numero) == -1:
        break
    else:
        numero = int(numero)
        numero_final = hex(numero)
        numero_final = numero_final[:2] + numero_final[2:].upper()
        print(str(numero_final))